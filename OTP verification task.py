import streamlit as st
import random

# Generate OTP
def generate_otp():
    otp = ""
    for _ in range(7):
        otp += str(random.randint(0, 9))
    return otp

# Verify OTP
def verify_otp(user_otp, generated_otp):
    return user_otp == generated_otp

st.set_page_config(page_title="OTP Verification System")

st.title("🔐 OTP Verification System")

phone_number = st.text_input("Enter Phone Number")

if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = None

if st.button("Generate OTP"):
    st.session_state.generated_otp = generate_otp()

    # Demo only
    st.success(f"OTP Generated: {st.session_state.generated_otp}")

    st.info(
        f"In production, OTP would be sent to {phone_number} using Twilio/Fast2SMS."
    )

user_otp = st.text_input("Enter OTP")

if st.button("Verify OTP"):

    if st.session_state.generated_otp is None:
        st.warning("Please generate OTP first.")

    elif verify_otp(user_otp, st.session_state.generated_otp):
        st.success("✅ OTP Verification Successful")

    else:
        st.error("❌ OTP Verification Failed")
