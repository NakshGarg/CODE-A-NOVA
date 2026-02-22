import smtplib
from email.message import EmailMessage

# -------------------------------
# Email Configuration
# -------------------------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"

RECEIVERS = [
    "receiver1@gmail.com",
    "receiver2@gmail.com"
]

# -------------------------------
# Create Email
# -------------------------------
msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(RECEIVERS)
msg["Subject"] = "Automated Email using Python 🚀"

msg.set_content("""
Hello,

This email was sent using a Python automation script.

Regards,
Python Script
""")

# -------------------------------
# Send Email
# -------------------------------
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error sending email:", e)
