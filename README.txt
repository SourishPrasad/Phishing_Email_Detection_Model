## 🛡️ Phishing Email Detection System
📌 Project Overview
An automated Machine Learning security tool designed to classify .eml files as Phishing or Safe. Developed as part of a Cybersecurity specialization at SRCAS.

🛠️ Technical Features
NLP Analysis: Uses TfidfVectorizer to identify malicious language patterns.

Heuristic Detection: Scans for high URL density and urgency-based keywords (e.g., Verify, Suspended).

Ensemble Model: Powered by a RandomForestClassifier for robust decision-making.

Confidence Scoring: Provides a probability percentage for every classification.

📊 Proven Results
During testing with the Zorvyn Internship Offer Letter, the model achieved:

Result: ✅ SAFE EMAIL

Confidence: 93.50%

Accuracy: 100% on current test-split.

🖥️ Example Output
Plaintext
==================================================
PHISHING EMAIL DETECTOR (.EML ONLY)
==================================================
File: Your Offer Letter for Cybersecurity Intern...
RESULT: ✅ SAFE EMAIL
CONFIDENCE: 93.50%
==================================================
🚀 Quick Start
Install: pip install scikit-learn pandas numpy

Run: python phishing_email_detector.py

Input: Enter the full path to any .eml file.

📂 Files
phishing_email_detector.py: Core ML logic.

requirements.txt: Dependencies.
