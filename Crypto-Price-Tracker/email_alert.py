import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_alert(price, threshold):
    sender = os.getenv("tyagiabhijeet78@gmail.com")
    receiver = os.getenv("tyagiabhijeet12@gmail.com")
    password = os.getenv("@abhijeet1212")

    subject = "Crypto Price Alert 🚨"
    body = f"Bitcoin price is now ${price}, which crossed your threshold of ${threshold}!"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

if __name__ == "__main__":
    send_email_alert(52000, 50000)
