# import streamlit as st
# from prediction_helper import predict
# import matplotlib.pyplot as plt
# import pyrebase

# # Page setup
# st.set_page_config(page_title="Divyam Finance: Credit Risk Modelling", page_icon="💼")
# st.title("💼 Divyam Finance: Credit Risk Modelling")
# st.markdown("Welcome to Divyam's Credit Risk Modelling tool! 🔍 Fill in the details below to assess risk.")


# firebaseConfig = {
#   "apiKey": "AIzaSyB3Qc-_-KVKf8fSwcgMQgsav_pP-tA1O7g",
#   "authDomain": "credit-risk-project-39947.firebaseapp.com",
#   "projectId": "credit-risk-project-39947",
#   "storageBucket": "credit-risk-project-39947.firebasestorage.app",
#   "messagingSenderId": "793782120938",
#   "appId": "1:793782120938:web:3e6c99ba6a259332478293",
#   "databaseURL": "https://dummy.firebaseio.com",
#   "measurementId": "G-DBK39Q1NGC"
# }


# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'user_email' not in st.session_state:
#     st.session_state.user_email = None

# # --- LOGIN SCREEN ---
# if not st.session_state.logged_in:
#     with st.expander("🔐 Login or Continue", expanded=True):
#         st.markdown("Choose how you'd like to proceed:")

#         # Email login
#         email = st.text_input("Email")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             try:
#                 user = auth.sign_in_with_email_and_password(email, password)
#                 st.success("✅ Logged in as " + user['email'])
#                 st.session_state.logged_in = True
#                 st.session_state.user_email = user['email']
#             except:
#                 st.error("❌ Invalid credentials. Try again.")

#         st.markdown("---")
        
#         # Guest access
#         if st.button("Continue as Guest"):
#             st.session_state.logged_in = True
#             st.session_state.user_email = "Guest"
        
#     st.stop()  # Stop rest of app until user logs in

# # --- WELCOME HEADER ---
# st.success(f"👋 Welcome, {st.session_state.user_email}")
# if st.button("Logout"):
#     st.session_state.logged_in = False
#     st.session_state.user_email = None
#     st.experimental_rerun()
# # --- Begin form ---
# with st.form("credit_form"):
#     row1 = st.columns(3)
#     row2 = st.columns(3)
#     row3 = st.columns(3)
#     row4 = st.columns(3)

#     # Row 1: Basic
#     with row1[0]:
#         age = st.number_input('🧍 Age', min_value=18, step=1, max_value=100, value=28)
#     with row1[1]:
#         income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000)
#     with row1[2]:
#         loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000)

#     # Row 2: Ratios
#     loan_to_income_ratio = loan_amount / income if income > 0 else 0
#     with row2[0]:
#         st.number_input('📈 Loan to Income Ratio', value=round(loan_to_income_ratio, 2), disabled=True)     
#     with row2[1]:
#         loan_tenure_months = st.number_input('⏳ Loan Tenure (months)', min_value=0, step=1, value=36)
#     with row2[2]:
#         avg_dpd_per_delinquency = st.number_input('📉 Avg DPD', min_value=0, value=20)

#     # Row 3: Financials
#     with row3[0]:
#         delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
#     with row3[1]:
#         credit_utilization_ratio = st.number_input('📊 Credit Utilization (%)', min_value=0, max_value=100, step=1, value=30)
#     with row3[2]:
#         num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

#     # Row 4: Categorical
#     with row4[0]:
#         residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])
#     with row4[1]:
#         loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
#     with row4[2]:
#         loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

#     # Submit button
#     submitted = st.form_submit_button("🚀 Calculate Risk")

# # --- On Submit ---
# if submitted:
#     probability, credit_score, rating = predict(
#         age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
#         delinquency_ratio, credit_utilization_ratio, num_open_accounts,
#         residence_type, loan_purpose, loan_type
#     )

#     # ✅ Text Summary
#     st.success("✅ Risk Prediction Complete!")
#     st.markdown(f"""
#     > Based on the inputs, the applicant is **{rating}** with a credit score of **{credit_score}**.
#     There is a **{probability:.2%}** chance of defaulting, which is considered **{'high' if probability > 0.5 else 'low'}**.
#     """)

#     # 📊 Chart
#     fig, ax = plt.subplots()
#     ax.bar(['Default Probability', 'Non-Default'], [probability, 1 - probability], color=['red', 'green'])
#     ax.set_ylim([0, 1])
#     st.pyplot(fig)

# # Footer
# st.markdown("---")
# st.markdown(
#     "<p style='text-align:center;'>🚧 Built with ❤️ by <a href='https://divyamsachdevaa.netlify.app' target='_blank'>Divyam Naveen Sachdeva</a> | "
#     "<a href='https://github.com/sachdevaaaa/divyam_finance' target='_blank'>GitHub Repo</a></p>",
#     unsafe_allow_html=True
# )


import streamlit as st
from prediction_helper import predict
import matplotlib.pyplot as plt
import pyrebase

# Page setup
st.set_page_config(page_title="Divyam Finance: Credit Risk Modelling", page_icon="💼")

# Style
st.markdown("""
    <style>
        div[data-testid="stMarkdownContainer"] > p {
            font-size: 17px;
        }
        label, .stTextInput > label {
            font-size: 16px !important;
        }
        .custom-button {
            margin-top: 20px;
        }
        .stButton > button {
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💼 Divyam Finance: Credit Risk Modelling")
st.markdown("Welcome to Divyam's Credit Risk Modelling tool! 🔍 Fill in the details below to assess risk.")

# Firebase config
firebaseConfig = {
    "apiKey": "AIzaSyB3Qc-_-KVKf8fSwcgMQgsav_pP-tA1O7g",
    "authDomain": "credit-risk-project-39947.firebaseapp.com",
    "projectId": "credit-risk-project-39947",
    "storageBucket": "credit-risk-project-39947.firebasestorage.app",
    "messagingSenderId": "793782120938",
    "appId": "1:793782120938:web:3e6c99ba6a259332478293",
    "databaseURL": "https://dummy.firebaseio.com",
    "measurementId": "G-DBK39Q1NGC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Session setup
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = None

# --- LOGIN SCREEN ---
if not st.session_state.logged_in:
    with st.expander("🔐 Login or Continue", expanded=True):
        st.markdown("Choose how you'd like to proceed:")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Login"):
                try:
                    user = auth.sign_in_with_email_and_password(email, password)
                    st.success("✅ Logged in as " + user['email'])
                    st.session_state.logged_in = True
                    st.session_state.user_email = user['email']
                    st.rerun()
                except:
                    st.error("❌ Invalid login credentials.")

        with col2:
            if st.button("Register"):
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    st.success("🎉 Registered successfully. Now log in.")
                except:
                    st.error("⚠️ Registration failed. Use valid email & a strong password (min 6 chars).")

        with col3:
            if st.button("Continue as Guest"):
                st.session_state.logged_in = True
                st.session_state.user_email = "Guest"
                st.rerun()

    st.stop()

# --- WELCOME ---
st.success(f"👋 Welcome, {st.session_state.user_email}")
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.rerun()

# --- FORM ---
with st.form("credit_form"):
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('🧍 Age', min_value=18, step=1, max_value=100, value=28)
    with row1[1]:
        income = st.number_input('💰 Annual Income (₹)', min_value=0, value=1200000)
    with row1[2]:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000)

    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    with row2[0]:
        st.number_input('📈 Loan to Income Ratio', value=round(loan_to_income_ratio, 2), disabled=True)
    with row2[1]:
        loan_tenure_months = st.number_input('⏳ Loan Tenure (months)', min_value=0, step=1, value=36)
    with row2[2]:
        avg_dpd_per_delinquency = st.number_input('📉 Avg DPD', min_value=0, value=20)

    with row3[0]:
        delinquency_ratio = st.number_input('⚠️ Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
    with row3[1]:
        credit_utilization_ratio = st.number_input('📊 Credit Utilization (%)', min_value=0, max_value=100, step=1, value=30)
    with row3[2]:
        num_open_accounts = st.number_input('📂 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

    with row4[0]:
        residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'])
    with row4[1]:
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
    with row4[2]:
        loan_type = st.selectbox('🔐 Loan Type', ['Unsecured', 'Secured'])

    submitted = st.form_submit_button("🚀 Calculate Risk")

# --- PREDICTION ---
if submitted:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.success("✅ Risk Prediction Complete!")
    st.markdown(f"""
    > Based on the inputs, the applicant is **{rating}** with a credit score of **{credit_score}**.  
    There is a **{probability:.2%}** chance of defaulting, which is considered **{'high' if probability > 0.5 else 'low'}**.
    """)

    fig, ax = plt.subplots()
    ax.bar(['Default Probability', 'Non-Default'], [probability, 1 - probability], color=['red', 'green'])
    ax.set_ylim([0, 1])
    st.pyplot(fig)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>🚧 Built with ❤️ by <a href='https://divyamsachdevaa.netlify.app' target='_blank'>Divyam Naveen Sachdeva</a> | "
    "<a href='https://github.com/sachdevaaaa/divyam_finance' target='_blank'>GitHub Repo</a></p>",
    unsafe_allow_html=True
)
