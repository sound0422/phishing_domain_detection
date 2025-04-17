# Phishing Domain Detection with Machine Learning  

## Objective

Phishing is a cyber-attack where a malicious actor impersonates a trusted entity to trick users into revealing sensitive information like login credentials or banking details. Instead of bypassing firewalls or complex security systems, attackers simply fool the user.

The objective of this project is to build a **domain authentication system** that can detect whether a given domain is legitimate or created for phishing. We evaluate multiple machine learning models, build a real-time web interface, and expose a REST API for broader integration.

---

## Project Workflow

This project follows a typical ML pipeline involving:

- Data Collection
- Feature Extraction
- Model Training & Evaluation
- Deployment

---

## Data Collection

- **Source**: Mendeley Data  
- [Dataset Link](https://data.mendeley.com/datasets/)  
- Size: 88,667 domain names  
- Labeled: 0 for legitimate, 1 for phishing  
- Features: 112 features available initially

---

## Feature Extraction

From the domain URLs, we engineered 18 features across the following categories:

- **Length-based Features** (e.g., domain length, digit count)
- **Count-based Features** (e.g., number of dots, special characters)
- **Binary Features** (e.g., has HTTPS, has IP)

Feature extraction is done using Python libraries such as:
- `tldextract`
- `re` (regex)
- `pandas`

_(Refer to the notebook for full list of engineered features)_

---

## Model Training

This is a binary classification task (0 = legitimate, 1 = phishing).

### ML Models Trained:
- Decision Tree
- Random Forest
- Multilayer Perceptron (MLP)
- XGBoost (**Best performing** model)

**Final Model**:  
- Algorithm: **XGBoostClassifier**  
- Accuracy: ~96.5% on test data  
- Files:  
  - `xgboost_model.pkl` (trained model)  
  - `scaler.pkl` (StandardScaler)

---

## To Run (Locally)

bash
# Clone the repository
```
git clone https://github.com/yourusername/phishing-domain-detector.git
cd phishing-domain-detector
```

# Create virtual environment (optional)
```
python -m venv venv
venv\Scripts\activate  # For Windows
 venv/bin/activate  # For Mac/Linux
 ```
 # Web Interface & API Documentation
We created a simple Flask web interface for testing the model in real time. It allows users to:
- Input any domain
- Get immediate prediction
- See if it's safe (0) or phishing (1)
The app uses:
1. Flask
2. HTML/CSS
3. Pickle files for prediction

# Install dependencies
```
pip install -r requirements.txt
```

# Run the app
```
python app.py
```
# Improvements to make
This project was developed as an end-to-end learning exercise, so model optimization wasn't the main focus. Here’s what can be improved going forward:

- Collect more recent and high-quality data with less sparsity.

- Apply feature selection to reduce dimensionality and boost performance.

- Optimize models further for better precision, especially in real-world applications.

- Experiment with advanced ML models or deep learning techniques.

- Enhance the API and UI for better user experience and scalability.