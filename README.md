# 🏦 Loan Default Risk Predictor

An XGBoost-powered credit risk assessment tool built specifically
for the Nigerian lending market — from microfinance to commercial facilities.

🔗 **Live App:** [Click to open](https://stephenudom-loan-default-predictor.streamlit.app/)

---

## What It Does

This tool predicts the probability that a borrower will default on a loan,
using a machine learning model trained on 1,600,000 synthetic Nigerian loan records
across four lending segments: micro, SME, salary, and commercial.

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
| AUC-ROC | 0.8928 |
| Recall (defaults caught) | 80.0% |
| Algorithm | XGBoost |
| Training records | 1,600,000 |
| Gender-neutral | Yes |

---

## How to Run Locally
```bash
git clone https://github.com/stephenudom/loan-default-risk-predictor
cd loan-default-risk-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## Built By

**Nkpo-ikana Udom** — Operations & Strategy | Fintech & Credit Risk  
[LinkedIn](https://www.linkedin.com/in/nkpo-ikana-udom-479ba91a9/) ·
[GitHub](https://github.com/stephenudom)
