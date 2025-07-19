import requests

def get_crypto_price(crypto_id="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id][currency]