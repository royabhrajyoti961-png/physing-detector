import streamlit as st
from model import predict_email

st.title("📧 AI Phishing Email Detector")

email = st.text_area("Paste Email Content")

if st.button("Analyze"):
    if email.strip() == "":
        st.warning("Please enter email text")
    else:
        result, confidence = predict_email(email)

        if result == 1:
            st.error(f"⚠️ Phishing Detected ({confidence*100:.2f}%)")
        else:
            st.success(f"✅ Safe Email ({confidence*100:.2f}%)")

        st.progress(int(confidence * 100))
