import streamlit as st
from backend import predict_price

# Streamlit UI
st.set_page_config(page_title="House Price Predictor", page_icon="🏡")
st.title("🏡 House Price Prediction")
st.write("Enter your house details and click **Predict** to estimate the price.")

with st.form("prediction_form"):
    # All in one column
    bedrooms = st.number_input("🛏 Bedrooms", min_value=0, value=3)
    bathrooms = st.number_input("🛁 Bathrooms", min_value=0, value=2)
    sqft_living = st.number_input("📐 Living Area (sqft)", min_value=0, value=1800)
    sqft_lot = st.number_input("🌳 Lot Area (sqft)", min_value=0, value=5000)
    floors = st.number_input("🏢 Floors", min_value=0, value=1)
    condition = st.slider("🏚 Condition Rating", 1, 5, 3)
    yr_built = st.number_input("🛠 Year Built", min_value=1800, value=1995)
    yr_renovated = st.number_input("🔧 Year Renovated (0 if never)", min_value=0, value=0)

    submitted = st.form_submit_button("🔮 Predict")

    if submitted:
        input_features = [
            bedrooms, bathrooms, sqft_living, sqft_lot,
            floors, condition, yr_built, yr_renovated
        ]

        prediction = predict_price(input_features)
        st.success(f"💰 Estimated House Price: **₹{prediction:,}**")
