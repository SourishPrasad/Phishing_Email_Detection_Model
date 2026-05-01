import os
import email
import re
import numpy as np
import pandas as pd
from email import policy
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import accuracy_score, classification_report

# ==========================================
# 1. EMAIL FEATURE EXTRACTION CLASS
# ==========================================
class EmailStructuralFeatures(BaseEstimator, TransformerMixin):
    """Extracts numerical features from email text (URLs, urgency keywords)."""
    def fit(self, x, y=None): return self
    def transform(self, posts):
        features = []
        for text in posts:
            text = str(text).lower()
            # Feature 1: Count links inside the email body
            url_count = len(re.findall(r'http[s]?://', text))
            # Feature 2: Count high-risk urgency keywords
            urgency = len(re.findall(r'(urgent|verify|action|suspend|security|login|password|expired|locked)', text))
            features.append([url_count, urgency])
        return np.array(features)

# ==========================================
# 2. EML PARSING LOGIC
# ==========================================
def parse_eml(file_path):
    """Extracts subject and body from .eml files for analysis."""
    try:
        with open(file_path, 'rb') as f:
            msg = email.message_from_binary_file(f, policy=policy.default)
        subject = msg.get('subject', '')
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_content()
                    break
        else:
            body = msg.get_content()
        return f"{subject} {body}".strip()
    except Exception as e:
        return f"Error parsing file: {e}"

# ==========================================
# 3. TRAINING PIPELINE
# ==========================================
def build_and_train():
    # Training dataset - Focused on Email content
    data = {
        'text': [
            "Your account is suspended. Verify now at http://secure-login.net",
            "Urgent security alert: Unauthorized login attempt detected.",
            "CONGRATULATIONS! You won a $500 gift card. Claim here: http://win-prize.biz",
            "Bank Alert: Your password has expired. Reset it at http://mybank.com",
            "Final notice: Your subscription will be cancelled unless you pay now.",
            "Identity verification required: click to secure your account.",
            "Meeting for tomorrow is moved to 10 AM in Room 4B.",
            "Can you send over the final draft of the report?",
            "Please review the attached invoice for your purchase.",
            "The project documentation is updated on the shared drive.",
            "Your Amazon order has been shipped. Track your package here.",
            "Happy birthday! Hope you have a great day.",
            "The weather in Coimbatore is perfect for a walk today.",
            "Please find the internship certificate attached.",
            "Team meeting notes have been uploaded to the portal."
        ],
        'label': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    df = pd.DataFrame(data)

    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('text_tfidf', TfidfVectorizer(stop_words='english')),
            ('structural', EmailStructuralFeatures())
        ])),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3, random_state=42)
    
    print("--- Model Training & Performance Report ---")
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Phishing']))
    
    return pipeline

# ==========================================
# 4. MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    model = build_and_train()
    
    print("\n" + "="*50)
    print("PHISHING EMAIL DETECTOR (.EML ONLY)")
    print("="*50)
    
    path = input("\nEnter the full path to the .eml file: ").strip().replace('"', '')

    if os.path.exists(path) and path.lower().endswith('.eml'):
        email_content = parse_eml(path)
        prediction = model.predict([email_content])[0]
        prob = model.predict_proba([email_content])[0]
        
        result = "⚠️ PHISHING DETECTED" if prediction == 1 else "✅ SAFE EMAIL"
        print("\n" + "="*50)
        print(f"FINAL RESULT: {result}")
        print(f"CONFIDENCE:   {prob[prediction]*100:.2f}%")
        print("="*50)
    else:
        print("\n❌ Error: Invalid input. Please provide a valid .eml file path.")