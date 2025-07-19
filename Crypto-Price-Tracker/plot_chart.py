import matplotlib.pyplot as plt

def plot_price_history(price_list):
    plt.plot(price_list, marker='o')
    plt.title("Crypto Price Trend")
    plt.xlabel("Time (auto refresh)")
    plt.ylabel("Price in USD")
    plt.grid()
    plt.savefig("price_trend.png")
    plt.close()