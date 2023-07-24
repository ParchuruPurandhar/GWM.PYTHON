import random
def generate_otp():
    """Generate a seven-digit OTP"""
    otp = ""
    for _ in range(7):
        otp += str(random.randint(0, 9))
    return otp
def send_otp_via_sms(otp, phone_number):
    """Simulate sending OTP via SMS"""
    print(f"Sending OTP {otp} to {phone_number} via SMS")
def verify_otp(user_otp, generated_otp):
    """Verify if the user-provided OTP matches the generated OTP"""
    return user_otp == generated_otp
phone_number = "+91 7032694836"  
otp = generate_otp()
send_otp_via_sms(otp, phone_number)
print("OTP has been sent to your phone number.")
user_otp = input("Enter the OTP you received: ")
if verify_otp(user_otp, otp):
    print("OTP verification successful.")
else:
    print("OTP verification failed.")