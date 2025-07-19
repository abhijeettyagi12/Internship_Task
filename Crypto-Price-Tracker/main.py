import time
from fetch_price import get_crypto_price
from email_alert import send_email_alert
from plot_chart import plot_price_history

price_history = []
alert_threshold = 50000  # Set your alert price

while True:
    price = get_crypto_price()
    print(f"Current Price: ${price}")
    price_history.append(price)

    if price >= alert_threshold:
        send_email_alert(price, alert_threshold)
        print("✅ Email Alert Sent!")

    if len(price_history) >= 10:
        plot_chart(price_history)
        print("📈 Chart Saved!")
        price_history = []

    time.sleep(60)  