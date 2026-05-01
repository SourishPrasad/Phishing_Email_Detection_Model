# 🛡️ Phishing Email Detection System
## 📌 Executive Summary
This project is an automated security tool developed to detect phishing attempts within raw email files (.eml). It utilizes a Machine Learning (ML) pipeline to perform deep content analysis, distinguishing between legitimate professional correspondence and malicious spoofing attempts. The model was designed to meet high-accuracy requirements for cybersecurity internship tasks, specifically focusing on textual and structural feature extraction.

## 🛠️ Technical Architecture
### 🧠 Natural Language Processing (NLP)
Vectorization: Uses TfidfVectorizer to tokenize and analyze the linguistic intent of the email body and subject lines.

### 🔍 Structural Heuristics
A custom feature engineering layer identifies "red flags" such as:

URL Density: Counting embedded links which are common in phishing vectors.

Urgency Analysis: Detecting high-pressure keywords like Verify, Suspended, Action Required, and Password.

### 🌲 Ensemble Modeling
Algorithm: Employs a RandomForestClassifier (100 estimators) to provide a robust, non-linear decision boundary for classification.

## 📊 Performance & Validation
The model provides real-time performance metrics using Scikit-learn's classification_report. During testing with legitimate internal documents—such as the Zorvyn Cybersecurity Analyst Intern Offer Letter—the model demonstrated:

Average Confidence: ~93.50%

Accuracy Score: Validated through a 70/30 train-test split.

## 🖥️ Example Output
Plaintext
--- Model Training & Performance Report ---
Accuracy: 100.00%
              precision    recall  f1-score   support

        Safe       1.00      1.00      1.00         3
    Phishing       1.00      1.00      1.00         2

==================================================
PHISHING EMAIL DETECTOR (.EML ONLY)
==================================================

Enter the full path to the .eml file: C:\Users\acer\Downloads\Your Offer Letter...

==================================================
🔍 ANALYSIS RESULTS
==================================================
FINAL RESULT: ✅ SAFE EMAIL
CONFIDENCE:   93.50%
==================================================
## 🚀 Installation & Usage
### 📋 Prerequisites
Python 3.10+

Libraries: scikit-learn, pandas, numpy

### ⚙️ Setup & Execution
Install dependencies: pip install -r requirements.txt

Run the script: python phishing_email_detector.py

## 📂 Project Structure
phishing_email_detector.py: Main application logic.

requirements.txt: Dependency manifest.

README.md: System documentation.
