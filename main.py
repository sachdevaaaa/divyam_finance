import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(page_title="Divyam Finance: Credit Risk Modelling", page_icon="💼")
st.title("💼 Divyam Finance: Credit Risk Modelling")

st.markdown("Welcome to Divyam's Credit Risk Modelling tool! 🔍 Fill in the details below to assess risk.")

# Create rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Row 1: Basic loan details
with row1[0]:
    age = st.number_input('🧍 Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000)

# Row 2: Ratios & tenure
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.markdown("**Loan to Income Ratio:**")
    st.code(f"{loan_to_income_ratio:.2f}")
with row2[1]:
    loan_tenure_months = st.number_input('⏳ Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('📉 Avg DPD', min_value=0, value=20)

# Row 3: More financial features
with row3[0]:
    delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('📊 Credit Utilization (%)', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

# Row 4: Categorical features
with row4[0]:
    residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

# Predict button
if st.button('🚀 Calculate Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.success("✅ Risk Prediction Complete!")
    st.write(f"**📉 Default Probability:** {probability:.2%}")
    st.write(f"**💳 Credit Score:** {credit_score}")
    st.write(f"**🏷️ Rating:** {rating}")

# Custom footer
st.markdown("---")
st.markdown("🚧 _Built with ❤️ by Divyam Naveen Sachdeva \n https://divyamsachdevaa.netlify.app/")
