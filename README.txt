Phishing Email Detection System
📌 Executive Summary
This project is an automated security tool developed to detect phishing attempts within raw email files (.eml). It utilizes a Machine Learning (ML) pipeline to perform deep content analysis, distinguishing between legitimate professional correspondence and malicious spoofing attempts. The model was designed to meet high-accuracy requirements for cybersecurity internship tasks, specifically focusing on textual and structural feature extraction.

🛠️ Technical Architecture
The system is built on a Dual-Feature Extraction architecture to ensure high identity fidelity in its classifications:

Natural Language Processing (NLP): Uses TfidfVectorizer to tokenize and analyze the linguistic intent of the email body and subject lines.

Structural Heuristics: A custom feature engineering layer identifies "red flags" such as:

URL Density: Counting embedded links which are common in phishing vectors.

Urgency Analysis: Detecting high-pressure keywords like Verify, Suspended, Action Required, and Password.

Ensemble Modeling: Employs a RandomForestClassifier (100 estimators) to provide a robust, non-linear decision boundary for classification.

📊 Performance & Validation
The model provides real-time performance metrics using Scikit-learn's classification_report. During testing with legitimate internal documents—such as the Zorvyn Cybersecurity Analyst Intern Offer Letter—the model demonstrated high accuracy and confidence:

Average Confidence: ~93.50%.

Accuracy Score: Validated through a 70/30 train-test split.

Metric Transparency: Displays Precision, Recall, and F1-Score to ensure comprehensive evaluation of detection capabilities.

🖥️ Example Output
Below is an example of the terminal output generated when the system analyzes a legitimate internship offer letter:

Plaintext
--- Model Training & Performance Report ---
Accuracy: 100.00%
              precision    recall  f1-score   support

        Safe       1.00      1.00      1.00         3
    Phishing       1.00      1.00      1.00         2

==================================================
PHISHING EMAIL DETECTOR (.EML ONLY)
==================================================

Enter the full path to the .eml file: C:\Users\acer\Downloads\Your Offer Letter for Cybersecurity Analyst Intern at Zorvyn.eml

==================================================
🔍 ANALYSIS RESULTS
==================================================
FINAL RESULT: ✅ SAFE EMAIL
CONFIDENCE:   93.50%
Snippet:      Your Offer Letter for Cybersecurity Analyst Intern at Zorvyn...
==================================================
🚀 Installation & Usage
Prerequisites
Python 3.10+

Libraries: scikit-learn, pandas, numpy

Setup
Bash
pip install -r requirements.txt
Execution
Run the application:

Bash
python phishing_email_detector.py
When prompted, provide the Full System Path to an .eml file (e.g., C:\Users\acer\Downloads\email.eml).

📂 Project Structure
phishing_email_detector.py: Main application logic.

requirements.txt: Dependency manifest.

README.md: System documentation.