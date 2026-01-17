import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.title("📉 Customer Churn Prediction App")

st.write("Enter customer details to predict churn")

# -----------------------------
# Input fields
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input("Age", min_value=18, max_value=100, value=35)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Membership_Years = st.number_input("Membership Years", value=2.0)
    Login_Frequency = st.number_input("Login Frequency", value=10.0)
    Session_Duration_Avg = st.number_input("Avg Session Duration", value=15.0)

with col2:
    Country = st.text_input("Country", "USA")
    City = st.text_input("City", "New York")
    Pages_Per_Session = st.number_input("Pages per Session", value=5.0)
    Cart_Abandonment_Rate = st.number_input("Cart Abandonment Rate", value=0.2)
    Wishlist_Items = st.number_input("Wishlist Items", value=3.0)

with col3:
    Total_Purchases = st.number_input("Total Purchases", value=20.0)
    Average_Order_Value = st.number_input("Average Order Value", value=150.0)
    Days_Since_Last_Purchase = st.number_input("Days Since Last Purchase", value=30.0)
    Discount_Usage_Rate = st.number_input("Discount Usage Rate", value=0.3)
    Signup_Quarter = st.selectbox("Signup Quarter", ["Q1", "Q2", "Q3", "Q4"])

# Remaining numeric fields
st.subheader("Additional Metrics")

Email_Open_Rate = st.number_input("Email Open Rate", value=0.4)
Returns_Rate = st.number_input("Returns Rate", value=0.05)
Customer_Service_Calls = st.number_input("Customer Service Calls", value=1.0)
Product_Reviews_Written = st.number_input("Product Reviews Written", value=2.0)
Social_Media_Engagement_Score = st.number_input("Social Media Engagement Score", value=60.0)
Mobile_App_Usage = st.number_input("Mobile App Usage", value=1.0)
Payment_Method_Diversity = st.number_input("Payment Method Diversity", value=2.0)
Lifetime_Value = st.number_input("Lifetime Value", value=5000.0)
Credit_Balance = st.number_input("Credit Balance", value=200.0)

# -----------------------------
# Create input DataFrame
# -----------------------------
input_data = pd.DataFrame([{
    "Age": Age,
    "Gender": Gender,
    "Country": Country,
    "City": City,
    "Membership_Years": Membership_Years,
    "Login_Frequency": Login_Frequency,
    "Session_Duration_Avg": Session_Duration_Avg,
    "Pages_Per_Session": Pages_Per_Session,
    "Cart_Abandonment_Rate": Cart_Abandonment_Rate,
    "Wishlist_Items": Wishlist_Items,
    "Total_Purchases": Total_Purchases,
    "Average_Order_Value": Average_Order_Value,
    "Days_Since_Last_Purchase": Days_Since_Last_Purchase,
    "Discount_Usage_Rate": Discount_Usage_Rate,
    "Returns_Rate": Returns_Rate,
    "Email_Open_Rate": Email_Open_Rate,
    "Customer_Service_Calls": Customer_Service_Calls,
    "Product_Reviews_Written": Product_Reviews_Written,
    "Social_Media_Engagement_Score": Social_Media_Engagement_Score,
    "Mobile_App_Usage": Mobile_App_Usage,
    "Payment_Method_Diversity": Payment_Method_Diversity,
    "Lifetime_Value": Lifetime_Value,
    "Credit_Balance": Credit_Balance,
    "Signup_Quarter": Signup_Quarter
}])

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Churn"):
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if pred == 1:
        st.error(f"❌ Churn: YES (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Churn: NO (Probability: {prob:.2%})")

