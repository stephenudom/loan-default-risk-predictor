# 🏦 Loan Default Risk Predictor

An XGBoost-powered credit risk assessment tool built specifically 
for the Nigerian lending market — from microfinance to commercial facilities.

🔗 **Live App:** [Click to open](https://rotech-loan-default-predictor.streamlit.app/)

---

## What It Does

This tool predicts the probability that a borrower will default on a loan, 
using a machine learning model trained on 307,511 real loan applications.

It features two interfaces:

- **Customer Application Mode** — A clean, guided form where applicants 
  submit their details and receive a confirmation. They never see the risk score.
- **Loan Officer Dashboard** — Full assessment view with risk score, 
  SHAP explainability, bureau verification status, and credit recommendations.

---

## Key Features

- 🔵 Dual interface: customer form + officer dashboard
- 🔐 BVN input with consent logging and bureau-verification ready
- 📊 SHAP explainability — shows exactly why a borrower was scored
- ⚙️ Adjustable risk thresholds to match institutional credit policy
- 🏦 Employment sector, income type, and delinquency recency captured
- ✅ Gender-neutral and CBN fair lending compliant
- 💰 No income ceiling — covers micro to commercial lending

---

## Model Performance

| Metric | Value |
|---|---|
| AUC-ROC | 0.7664 |
| Recall (defaults caught) | 65.3% |
| Algorithm | XGBoost |
| Training records | 307,511 |
| Gender-neutral | Yes |

---

## How to Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/loan-default-risk-predictor
cd loan-default-risk-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## Built By

**Abiola Lawal** — Data Scientist | Credit Risk & Fintech ML  
[LinkedIn](https://linkedin.com/in/abiola-lawal-abdulrafiu) · 
[GitHub](https://github.com/abiolalawal14)
