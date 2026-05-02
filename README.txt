# 🛡️ Phishing Email Detection System

## 📌 Project Overview

An automated Machine Learning–based cybersecurity tool that classifies `.eml` email files as **Phishing** or **Safe**.
Developed as part of a Cybersecurity specialization at **SRCAS**, this project combines NLP, heuristic analysis, and ensemble learning to detect suspicious email patterns with confidence scoring.

---

## 🛠️ Technical Features

### **NLP-Based Content Analysis**

Utilizes **TfidfVectorizer** to extract and analyze malicious linguistic patterns commonly found in phishing emails.

### **Heuristic Threat Detection**

Scans emails for:

* High URL density
* Urgency / fear-based keywords
* Common phishing indicators such as:

  * `Verify`
  * `Suspended`
  * `Immediate Action Required`

### **Ensemble Machine Learning Model**

Powered by **RandomForestClassifier** for robust and reliable classification.

### **Confidence Scoring**

Outputs a probability percentage indicating the model’s confidence in each prediction.

---

## 📊 Performance Metrics

Tested using the **Zorvyn Internship Offer Letter** sample:

* **Classification Result:** ✅ Safe Email
* **Confidence Score:** 93.50%
* **Model Accuracy:** 100% on current test split

> **Note:** Accuracy is based on the present dataset/test split and may vary with broader real-world phishing samples.

---

## 🖥️ Example Output

```plaintext
==================================================
PHISHING EMAIL DETECTOR (.EML ONLY)
==================================================
File: Your Offer Letter for Cybersecurity Intern...
RESULT: ✅ SAFE EMAIL
CONFIDENCE: 93.50%
==================================================
```

---

## 🚀 Quick Start

### Install Dependencies

```bash
pip install scikit-learn pandas numpy
```

### Run the Program

```bash
python phishing_email_detector.py
```

### Input Format

Provide the **full file path** to any `.eml` email file when prompted.

---

## 📂 Project Structure

```plaintext
phishing_email_detector.py   # Core ML detection engine
requirements.txt             # Project dependencies
```

---

## 🎯 Purpose

This project demonstrates the practical application of:

* Machine Learning in Cybersecurity
* NLP for Threat Detection
* Email Security Automation
* Heuristic-Based Risk Analysis
