import streamlit as st 

import pandas as pd  
import pickle

with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Bank Term Deposit Subscription Prediction')

st.write('Fill out the following information to predict whether a customer at the bank will subscribe to the term deposit or not')

col1, col2, col3 = st.columns(3)
default = col1.selectbox('Credit in Default?', ['Yes', 'No'])
balance = col2.number_input('Balance ($)', value=0.0)
housing = col3.selectbox('Housing Loan?', ['Yes', 'No'])


col4, col5, col6  = st.columns(3)
loan = col4.selectbox('Personal Loan?', ['Yes', 'No'])
duration = col5.number_input('Call Duration (in seconds)', value=0.0)
poutcome = col6.selectbox('Previous Campaign Success?', ['No', 'Yes'])


col7, col8, col9 = st.columns(3)
contacted_before = col7.selectbox('Contacted Before?', ['Yes', 'No'])
contacted_recently = col8.selectbox('Contacted Recently?', ['Yes', 'No'])
is_employed = col9.selectbox('Is Employed?', ['Yes', 'No'])

col10, col11, col12 = st.columns(3)
is_married = col10.selectbox('Is Married?', ['Yes', 'No'])
is_graduate = col11.selectbox('Is Graduate?', ['Yes', 'No'])

input_data = pd.DataFrame([{
    'default': 1 if default == 'Yes' else 0,
    'balance': balance,
    'housing': 1 if housing == 'Yes' else 0,
    'loan': 1 if loan == 'Yes' else 0,
    'duration': duration,
    'poutcome': 1 if poutcome == 'Yes' else 0,
    'contacted_before': 1 if contacted_before == 'Yes' else 0,
    'contacted_recently': 1 if contacted_recently == 'Yes' else 0,
    'is_employed': 1 if is_employed == 'Yes' else 0,
    'is_married': 1 if is_married == 'Yes' else 0,
    'is_graduate': 1 if is_graduate == 'Yes' else 0,
}])

if st.button('Predict Subscription'):
    prediction = model.predict(input_data)
    result = "Yes" if prediction[0] == 1 else "No"
    st.success(f"Term deposit subscription status for this client: {result}")


