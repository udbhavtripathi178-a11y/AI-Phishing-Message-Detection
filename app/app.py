
import streamlit as st
from src.prediction.predict import predict_message

# Page configuration
st.set_page_config(
    page_title="AI Phishing Detection",
    page_icon="🛡️",
    layout="centered"
)

# Session state for prediction history
if "history" not in st.session_state:
    st.session_state.history = []

# Header
st.title("🛡️ AI Phishing Message Detection")

st.caption("SIC AI Capstone Project | Version 1.0")

st.write(
    "Analyse SMS messages using a Machine Learning model "
    "and identify their predicted category."
)

st.divider()

# Message input
st.subheader("Message Analysis")

message = st.text_area(
    "Enter your message",
    placeholder="Paste your SMS or message here...",
    height=150
)

# Prediction
if st.button("🔍 Analyse Message", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        result = predict_message(message)

        st.session_state.history.insert(
            0,
            {"message": message, "prediction": result}
        )

        st.subheader("Detection Result")

        if result == "ham":
            st.success("✅ Predicted Category: Legitimate (Ham)")

        elif result == "spam":
            st.warning("⚠️ Predicted Category: Spam")

        elif result == "smishing":
            st.error("🚨 Predicted Category: Smishing")

        st.caption(
            "This is an automated model prediction, "
            "not a guaranteed security verdict."
        )

# Prediction history
st.divider()
st.subheader("Recent Prediction History")

if st.session_state.history:

    for item in st.session_state.history[:10]:

        st.write("**Message:**", item["message"])
        st.write("**Prediction:**", item["prediction"])
        st.divider()

else:
    st.info("No messages analysed yet.")

# Security notice
st.subheader("Security Notice")

st.warning(
    "Never share OTPs, passwords, banking credentials, "
    "or sensitive personal information. Do not click "
    "suspicious links based only on this model's prediction."
)

st.caption(
    "Developed as an academic AI/ML project. "
    "Predictions may be incorrect."
)
