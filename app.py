
import pickle
import numpy as np
from xgboost import XGBClassifier
import re 
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the saved model and scaler
with open('xgboost_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

# Feature extraction function
import tldextract
import re
import numpy as np

def extract_features(domain):
    features = []

    # Ensure domain has a valid structure (has a TLD and dot)
    if '.' not in domain:
        return np.array([[-1]*13])  # Invalid domain format
    
    # 1. length_url
    features.append(len(domain))

    # 2. domain_length
    ext = tldextract.extract(domain)
    features.append(len(ext.domain))  # Length of the main domain part (excluding subdomain and TLD)

    # 3. domain_in_ip
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    features.append(1 if re.fullmatch(ip_pattern, domain) else 0)

    # 4. directory_length, 5. file_length, 6. params_length
    # Placeholder for now, you can update as needed
    features.extend([0, 0, 0])

    # 7. email_in_url
    features.append(1 if "@" in domain else 0)

    # 8. asn_ip
    features.append(0)  # Placeholder

    # 9. time_domain_activation, 10. time_domain_expiration → placeholders
    features.extend([0, 0])

    # 11. tls_ssl_certificate
    features.append(0)  # Placeholder

    # 12. qty_redirects
    features.append(0)  # Placeholder

    # 14. qty_char_domain (removes non-alphanumeric characters)
    features.append(len(re.sub(r'\W+', '', ext.domain)))  # Use domain part (exclude subdomain)

    return np.array([features])



@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        domain = request.form['domain']  # Get the domain from the input field
        if not domain:  # Check if the domain is empty
            return render_template('index.html', prediction="Please enter a domain.")  # Provide a message if empty

        # If the domain is not empty, extract features and scale them
        features = extract_features(domain)
        scaled_features = scaler.transform(features)  # Scale the extracted features using the loaded scaler

        # Make prediction
        prediction = model.predict(scaled_features)

        # Display the prediction
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html', prediction="")

if __name__ == '__main__':
    app.run(debug=True)
