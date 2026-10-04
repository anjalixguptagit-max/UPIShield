# 🛡️ UPIShield

### AI-Powered UPI Fraud Detection & Risk Analysis Prototype

UPIShield is an intelligent UPI transaction risk analysis system designed to identify potentially suspicious transactions and provide an understandable risk assessment.

The project combines rule-based risk scoring with machine learning experimentation to demonstrate how suspicious UPI transactions can be detected and analyzed.

---

## 🚨 Problem Statement

UPI transactions have grown rapidly, making digital payments faster and more convenient. However, the increasing transaction volume also creates opportunities for fraudulent and suspicious activities.

Traditional fraud detection systems may not always provide an easy-to-understand explanation of why a transaction was considered risky.

UPIShield aims to provide a simple and explainable approach to transaction risk detection.

---

## 💡 Our Solution

UPIShield analyzes transaction attributes such as:

- 💰 Transaction Amount
- 🕐 Transaction Time
- 📱 Device Type
- 🌐 Network Type
- 💳 Transaction Type
- 📅 Weekend/Weekday

Based on these factors, the system generates a risk score and classifies the transaction as:

- 🟢 **LOW RISK**
- 🟡 **MEDIUM RISK**
- 🔴 **HIGH RISK**

The system also provides reasons explaining why a transaction received a particular risk level.

---

## ⚙️ How It Works

```text
User Transaction Details
          ↓
Transaction Feature Analysis
          ↓
Risk Scoring Engine
          ↓
Risk Score Calculation
          ↓
┌─────────┬──────────┬─────────┐
│ LOW     │ MEDIUM   │ HIGH    │
│ RISK    │ RISK     │ RISK    │
└─────────┴──────────┴─────────┘
          ↓
Explainable Risk Reasons
```

---

## 📊 Dataset

The project includes analysis of a UPI transaction dataset containing:

- **250,000 transactions**
- **17 transaction attributes**
- **480 fraudulent transactions**
- **Fraud rate: 0.192%**
- **Average transaction amount: ₹1,311.76**
- **Maximum transaction amount: ₹42,099**

### Fraud Rate by Transaction Type

| Transaction Type | Fraud Rate |
|---|---:|
| Recharge | 0.239% |
| Bill Payment | 0.206% |
| P2M | 0.191% |
| P2P | 0.183% |

---

## 🧠 Risk Scoring

The current prototype uses an explainable rule-based scoring system.

| Condition | Risk Score |
|---|---:|
| Amount > ₹5,000 | +2 |
| Late-night transaction | +2 |
| Web device | +1 |
| WiFi network | +1 |
| Weekend transaction | +1 |

### Risk Classification

| Score | Risk Level |
|---:|---|
| 0–1 | 🟢 LOW |
| 2–3 | 🟡 MEDIUM |
| 4+ | 🔴 HIGH |

The system also displays the factors responsible for increasing the risk score.

---

## 🤖 Machine Learning

Machine learning models were also experimented with on the transaction dataset.

Because fraudulent transactions represent only a very small portion of the dataset, the dataset has a significant class imbalance.

Therefore, high overall accuracy alone cannot be considered a reliable indicator of fraud detection performance.

This project highlights the importance of metrics such as:

- Precision
- Recall
- F1-Score
- Confusion Matrix

especially for highly imbalanced fraud detection problems.

---

## ✨ Key Features

- 🔍 Transaction risk analysis
- 🚨 Fraud-risk classification
- 📊 Interactive dashboard
- 🧠 Explainable risk scoring
- 📈 Transaction data analysis
- 🤖 Machine learning experimentation
- ⚡ Fast risk assessment
- 🎯 User-friendly interface

---

## 🛠️ Technology Stack

### Frontend / Interface
- Streamlit

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Machine Learning
- Scikit-learn

### Visualization
- Matplotlib
- Seaborn

### Model/Data Utilities
- Joblib
- Jupyter Notebook

---

## 📁 Project Structure

```text
UPIShield/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── upi_transactions_2024.csv
│
├── notebooks/
│   └── UPI_Fraud_Detection.ipynb
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd UPIShield
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📌 Future Scope

UPIShield can be further enhanced with:

- 🔄 Real-time transaction stream processing
- 🧠 Advanced machine learning models
- 🌐 Graph-based fraud detection
- 📱 Device and user behavior profiling
- 🔐 Network and location-based anomaly detection
- 📈 Continuous model improvement
- ⚡ Real-time fraud alerts
- 🤖 Online learning for evolving fraud patterns

---

## 🎯 Project Vision

UPIShield aims to move beyond simple fraud detection by making transaction risk **explainable, understandable, and actionable**.

### Detect → Explain → Improve

---

## 👨‍💻 Presented By

**Anjali Gupta**  
**(24EACAD009)**  
**(Branch – AIDS)**

---

## 🏆 Hackathon Project

**UPIShield — AI-powered UPI Fraud Detection & Risk Analysis**

Built as a hackathon prototype to demonstrate an explainable approach to detecting suspicious UPI transactions.
