# Mean Reversion Strategy using Pairs Trading of BTC and ETH
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
frames = {}

def create_frame(ticker_input, start_date, end_date):
    ticker = yf.Ticker(ticker_input)
    data = ticker.history(start = start_date, end = end_date)
    return pd.DataFrame(data)

def scatter_plot(asset1, asset2):
    sns.jointplot(x=asset1, y=asset2, kind='scatter', color='blue')
    plt.xlabel("BTC Close Price")
    plt.ylabel("ETH Close Price")
    plt.title("Jointplot of BTC and ETH Close Prices")
    plt.show()

frames["btc"] = create_frame("BTC-USD", "2018-01-01", "2023-06-30")
frames["eth"] = create_frame("ETH-USD", "2018-01-01", "2023-06-30")

# Data Cleaning
for frame in frames:
    del frames[frame]["Dividends"]
    del frames[frame]["Stock Splits"]

def calculate_correlation(asset1, asset2, column):
    btc_close = frames[asset1][column]
    eth_close = frames[asset2][column]
    return eth_close.corr(btc_close)

def entry_exit_conditions(asset1, asset2, entry_threshold, exit_threshold, column):
    btc_close = frames[asset1][column]
    eth_close = frames[asset2][column]

    # Calculate Bollinger Bands
    window = 20  # Adjust this value for your desired window size
    btc_sma = btc_close.rolling(window=window, min_periods=1).mean()
    btc_std = btc_close.rolling(window=window, min_periods=1).std()
    eth_sma = eth_close.rolling(window=window, min_periods=1).mean()
    eth_std = eth_close.rolling(window=window, min_periods=1).std()

    # Generate trading signals
    signals = pd.Series(0, index=btc_close.index)

    # Long BTC and short ETH when BTC price is below the lower Bollinger Band and ETH price is above the upper Bollinger Band
    signals[(btc_close < btc_sma - entry_threshold * btc_std) & (eth_close > eth_sma + entry_threshold * eth_std)] = 1

    # Short BTC and long ETH when BTC price is above the upper Bollinger Band and ETH price is below the lower Bollinger Band
    signals[(btc_close > btc_sma + entry_threshold * btc_std) & (eth_close < eth_sma - entry_threshold * eth_std)] = -1

    # Exit signals when BTC and ETH prices move back within the exit_threshold range of their respective means
    exit_condition = (btc_close >= btc_sma - exit_threshold * btc_std) & (btc_close <= btc_sma + exit_threshold * btc_std) & \
                     (eth_close >= eth_sma - exit_threshold * eth_std) & (eth_close <= eth_sma + exit_threshold * eth_std)
    signals[exit_condition] = 0

    return signals


def calculate_daily_returns(asset1, asset2, signals, column):
    btc_close = frames[asset1][column]
    eth_close = frames[asset2][column]

    # Ensure all variables are Pandas Series or DataFrames
    signals = pd.Series(signals, index=btc_close.index)  # Convert signals to a Pandas Series
    btc_returns = btc_close.pct_change().shift(-1)
    eth_returns = eth_close.pct_change().shift(-1)
    daily_returns = signals * (btc_returns - eth_returns)

    # Count total number of trades
    total_trades = (signals != 0).sum()

    print("Total Number of Trades:", total_trades)

    return daily_returns


def plot_cumulative_returns(cumulative_returns):
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_returns.index, cumulative_returns, label="Cumulative Returns", color="green")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.title("Cumulative Returns for Pairs Trading Strategy")
    plt.legend()
    plt.grid(True)
    plt.show()

# Entry and Exit Conditions - Z-score Method
entry_threshold = 0.6
exit_threshold = 0.22

signals = entry_exit_conditions("btc", "eth", entry_threshold, exit_threshold, "Close")
daily_returns = calculate_daily_returns("btc", "eth", signals, "Close")
cumulative_returns = (1 + daily_returns).cumprod()
daily_returns_percent = daily_returns.sum() * 100
print(f"Overall profit: {daily_returns_percent.round(2)} %")
