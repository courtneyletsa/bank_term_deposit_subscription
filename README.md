# bank_term_deposit_subscription

This project predicts whether a client will subscribe to a bank term deposit based on historical marketing campaign data. It leverages a **Random Forest Classifier** trained on engineered features and provides an interactive **Streamlit web application** for predictions.

---

## Live Demo

**Try the Streamlit App:** [termdeposit.streamlit.app](https://termdeposit.streamlit.app)

---

## Machine Learning Model

I used a **Random Forest Classifier** trained on features such as:

- Credit in default
- Normalized account balance
- Housing and personal loan status
- Call duration
- Previous campaign success
- Contacted before or recently
- Employment, marital, and education status

Data preprocessing includes:
- Log transformation of skewed features (`balance`, `duration`)
- Label encoding categorical features
- Feature engineering of employment, marital status, and prior contacts
- Handling class imbalance with **RandomOverSampler**

---


## Streamlit App

The Streamlit app allows users to input client data and receive a real-time prediction on whether the client is likely to subscribe to a term deposit.

### How to Run Locally

1. **Install requirements:**

   ```bash
   pip install -r requirements.txt
