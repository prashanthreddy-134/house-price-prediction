import streamlit as st
from model import HousePriceModel


# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# -------------------------------------------------
# Custom styling
# -------------------------------------------------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            color: #9ca3af;
            font-size: 16px;
            margin-bottom: 25px;
        }

        .price-box {
            padding: 22px;
            border-radius: 14px;
            background: #123d2b;
            border: 1px solid #1f6b4a;
            text-align: center;
            margin-top: 20px;
        }

        .price-label {
            font-size: 15px;
            color: #a7f3d0;
        }

        .price-value {
            font-size: 34px;
            font-weight: 700;
            color: #34d399;
        }

        .info-box {
            padding: 15px;
            border-radius: 10px;
            background: #20242c;
            margin-top: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown(
    '<div class="main-title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine learning based house price estimation'
    '</div>',
    unsafe_allow_html=True
)


# -------------------------------------------------
# Model loading
# -------------------------------------------------
try:
    model = HousePriceModel()

except FileNotFoundError as e:
    st.error(str(e))
    st.stop()


# -------------------------------------------------
# Model information
# -------------------------------------------------
with st.expander("🤖 Model Information"):

    st.write("**Selected model:** Linear Regression")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("R² Score", "0.9953")

    with col2:
        st.metric("MAE", "₹3.60 L")

    with col3:
        st.metric("RMSE", "₹4.56 L")

    st.caption(
        "Metrics are calculated on the held-out test set from the project dataset."
    )


# -------------------------------------------------
# Input section
# -------------------------------------------------
st.subheader("Enter Property Details")

col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        max_value=10000,
        value=1500,
        step=100
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=8,
        value=2,
        step=1
    )


with col2:

    age = st.number_input(
        "House age (years)",
        min_value=0,
        max_value=100,
        value=10,
        step=1
    )

    parking = st.number_input(
        "Parking spaces",
        min_value=0,
        max_value=5,
        value=1,
        step=1
    )

    location = st.selectbox(
        "Location",
        [
            "Hyderabad",
            "Bengaluru",
            "Chennai",
            "Pune",
            "Delhi"
        ]
    )


# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button(
    "🔮 Predict House Price",
    use_container_width=True
):

    features = {
        "area_sqft": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "parking": parking,
        "location": location
    }

    try:

        prediction = model.predict(features)

        # Prevent negative predictions
        prediction = max(0, prediction)

        # -------------------------------------------------
        # Prediction result
        # -------------------------------------------------
        st.markdown(
            f"""
            <div class="price-box">
                <div class="price-label">
                    Estimated Property Price
                </div>
                <div class="price-value">
                    ₹{prediction:,.0f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # Input summary
        # -------------------------------------------------
        st.subheader("📋 Property Summary")

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:
            st.metric("Area", f"{area:,} sq ft")
            st.metric("Bedrooms", bedrooms)

        with summary_col2:
            st.metric("Bathrooms", bathrooms)
            st.metric("Parking", parking)

        with summary_col3:
            st.metric("Age", f"{age} years")
            st.metric("Location", location)

    except Exception as e:
        st.error(f"Prediction failed: {e}")


# -------------------------------------------------
# Dataset disclaimer
# -------------------------------------------------
st.markdown("---")

st.warning(
    "⚠️ This project uses a synthetic educational dataset. "
    "The predictions should not be treated as real-world property valuations."
)


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption(
    "House Price Prediction • Machine Learning Portfolio Project"
)