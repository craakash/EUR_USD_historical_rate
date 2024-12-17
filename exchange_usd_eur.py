import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Function to fetch EUR/USD exchange rate data using yfinance
def get_exchange_data(start_date, end_date):
    ticker = "EURUSD=X"  # Ticker for EUR/USD exchange rate
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.reset_index()
    data = data[['Date', 'Close']]  # Keep Date and Close columns
    return data

# Main execution
try:
    # Define date range for the last 5 years
    start_date = (datetime.datetime.now() - datetime.timedelta(days=5*365)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Fetch EUR/USD exchange rate data
    eur_usd = get_exchange_data(start_date, end_date)

    # Plot the EUR/USD exchange rate
    plt.figure(figsize=(12, 6))
    plt.plot(eur_usd['Date'], eur_usd['Close'], label='EUR/USD Exchange Rate', color='orange')
    plt.title('EUR to USD Exchange Rate (Last 5 Years)')
    plt.xlabel('Year')
    plt.ylabel('Exchange Rate (EUR to USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Determine the percentage change over the 5-year period
    initial_rate = eur_usd['Close'].iloc[0]
    final_rate = eur_usd['Close'].iloc[-1]
    percentage_change = ((final_rate - initial_rate) / initial_rate) * 100

    print(f"Initial Exchange Rate (5 years ago): {initial_rate:.2f}")
    print(f"Current Exchange Rate: {final_rate:.2f}")
    print(f"Percentage Change in EUR/USD: {percentage_change:.2f}%")

except Exception as e:
    print("An error occurred:", e)
