import streamlit as st
import pandas as pd
import random
import time

# --- Placeholder classes for CLV ---
class CustomData:
    def __init__(self, customer_id, quantity, unit_price, country, invoice_month):
        self.customer_id = customer_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.country = country
        self.invoice_month = invoice_month

    def get_data_as_data_frame(self):
        return pd.DataFrame({
            'CustomerID': [self.customer_id],
            'Quantity': [self.quantity],
            'UnitPrice': [self.unit_price],
            'Country': [self.country],
            'InvoiceMonth': [self.invoice_month]
        })

class PredictPipeline:
    def predict(self, features):
        # Placeholder: random CLV for demo
        return [round(random.uniform(100, 10000), 2)]

# --- Recommendation Logic ---
def generate_recommendations(clv_value):
    if clv_value < 2000:
        return [
            "🎁 Offer small discounts to encourage repeat purchases.",
            "📢 Send personalized marketing emails with product bundles.",
            "💡 Focus on increasing purchase frequency."
        ]
    elif 2000 <= clv_value < 6000:
        return [
            "🎉 Provide loyalty rewards to strengthen customer relationship.",
            "🛒 Recommend complementary products based on past purchases.",
            "🚚 Offer free/discounted shipping on next order."
        ]
    else:
        return [
            "👑 Treat as VIP: Provide exclusive offers and early access.",
            "💳 Suggest premium products and subscription models.",
            "🤝 Assign personalized account manager for retention."
        ]

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="Customer Lifetime Value Predictor",
    page_icon="🔮",
    layout="centered",
)

# --- Custom CSS for a new, bright color scheme and compact layout with neat boxes ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #e0f7fa; /* Light cyan background */
        color: #1a237e; /* Dark blue text */
    }
    
    .stApp {
        background-color: #e0f7fa;
    }

    .container-card {
        background-color: #ffffff; /* White background for the card */
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 25px;
        border: 1px solid #b0bec5;
    }
    
    .main-title {
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        color: #ff007f; /* Bright pink */
        text-shadow: 2px 2px 4px rgba(255, 0, 127, 0.3);
        margin-bottom: 5px;
    }
    
    .subtitle {
        text-align: center;
        color: #4db6ac;
        font-size: 1em;
        margin-bottom: 30px;
    }

    .prediction-box {
        background-color: #fce4ec; /* Light pink */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #ff4081; /* Hot pink */
        box-shadow: 0 0 10px rgba(255, 64, 129, 0.4);
        margin-top: 20px;
    }
    
    .clv-value {
        font-size: 2em;
        font-weight: bold;
        color: #ff4500; /* Vibrant orange-red color */
        text-shadow: 1px 1px 3px rgba(255, 69, 0, 0.5);
    }
    
    .stButton > button {
        background-color: #ff4081;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #e91e63;
        transform: scale(1.05);
    }
    
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #1a237e;
        font-weight: 600;
    }
    
    .stTextInput input, .stNumberInput input, .stSelectbox > div {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #b0bec5;
        border-radius: 5px;
        font-size: 0.9em;
    }
    
    .stProgress > div > div > div > div {
        background-color: #00ff7f;
    }
    
    .stExpander {
        border-radius: 10px;
        background-color: #f1f8e9; /* Light green */
        border: 1px solid #d4e157;
        margin-top: 20px;
    }

    .stExpander button {
        color: #827717;
    }
    
    .st-emotion-cache-12fmj77 {
        margin-top: -15px;
    }

</style>
""", unsafe_allow_html=True)

# --- Main Page Layout ---
st.markdown("<h1 class='main-title'>CLV Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Estimate customer value with bright insights.</p>", unsafe_allow_html=True)

# Using st.container for neat, organized boxes
col1, col2 = st.columns(2)

with col1:
    with st.container(border=False):
        st.markdown("<h5 style='color:#01579b; font-weight: bold;'>Customer & Purchase Details</h5>", unsafe_allow_html=True)
        customer_id = st.text_input("🆔 Customer ID")
        quantity = st.number_input("📦 Quantity Purchased", min_value=1, step=1)
        unit_price = st.number_input("💵 Unit Price", min_value=0.0, step=0.5)
    
with col2:
    with st.container(border=False):
        st.markdown("<h5 style='color:#01579b; font-weight: bold;'>Location & Date</h5>", unsafe_allow_html=True)
        country = st.selectbox("🌍 Country", ["United Kingdom", "France", "Germany", "Spain", "Other"])
        invoice_month = st.selectbox("🗓️ Invoice Month", 
                                     ["January", "February", "March", "April", "May", "June",
                                      "July", "August", "September", "October", "November", "December"])
    
st.write("") # Add a small spacer
st.write("")
submitted = st.button("🔮 Predict CLV")

# --- Prediction Logic and Output ---
if submitted:
    with st.spinner('Calculating...'):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        progress_bar.empty()

    data = CustomData(customer_id, quantity, unit_price, country, invoice_month)
    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)[0]

    # Display the prediction in a stylish box
    st.markdown(
        f"""
        <div class="prediction-box">
            <h4>Predicted CLV for customerid {customer_id}:</h4>
            <span class="clv-value">${result}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Use an expander for recommendations
    with st.expander("Click for Recommendations"):
        recs = generate_recommendations(result)
        st.markdown(
            """
            <h5 style="color:#00897b;">Strategies based on this CLV:</h5>
            """,
            unsafe_allow_html=True
        )
        for rec in recs:
            st.markdown(f"- **{rec}**")