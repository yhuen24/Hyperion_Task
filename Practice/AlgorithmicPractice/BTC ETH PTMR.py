# Mean Reversion Strategy using Pairs Trading of BTC and ETH
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
frames = {}


def create_frame(ticker_input, start_date, end_date):
    ticker = yf.Ticker(ticker_input)
    data = ticker.history(start=start_date, end=end_date)
    return pd.DataFrame(data)


def scatter_plot(asset1, asset2):
    sns.jointplot(x=asset1, y=asset2, kind='scatter', color='blue')
    plt.xlabel("BTC Close Price")
    plt.ylabel("ETH Close Price")
    plt.title("Jointplot of BTC and ETH Close Prices")
    plt.show()


frames["btc"] = create_frame("BTC-USD", "2018-01-01", "2023-06-30")
frames["eth"] = create_frame("ETH-USD", "2018-01-01", "2023-06-30")
print(frames["btc"])
# Data Cleaning
for frame in frames:
    del frames[frame]["Dividends"]
    del frames[frame]["Stock Splits"]


def calculate_correlation(asset1, asset2, column):
    btc_close = frames[asset1][column]
    eth_close = frames[asset2][column]
    return eth_close.corr(btc_close)


def entry_exit_conditions(asset1, asset2, entry_threshold, exit_threshold, column):
    asset1_close = frames[asset1][column]
    asset2_close = frames[asset2][column]

    # Calculate Bollinger Bands
    window = 21  # Moving Average Time Frame
    asset1_sma = asset1_close.rolling(window=window, min_periods=1).mean()
    asset1_std = asset1_close.rolling(window=window, min_periods=1).std()
    asset2_sma = asset2_close.rolling(window=window, min_periods=1).mean()
    asset2_std = asset2_close.rolling(window=window, min_periods=1).std()

    # Generate trading signals
    signals = pd.Series(0, index=asset1_close.index)

    # Long ass1 and short ass2 when ass1 price is below the lower Bollinger Band and ass2 price is above the upper Bollinger Band
    signals[(asset1_close < asset1_sma - entry_threshold * asset1_std) & (
            asset2_close > asset2_sma + entry_threshold * asset2_std)] = 1

    # Short as11 and long ass2 when ass1 price is above the upper Bollinger Band and ass2 price is below the lower Bollinger Band
    signals[(asset1_close > asset1_sma + entry_threshold * asset1_std) & (
            asset2_close < asset2_sma - entry_threshold * asset2_std)] = -1

    # Exit signals when BTC and ETH prices move back within the exit_threshold range of their respective means
    exit_condition = (asset1_close >= asset1_sma - exit_threshold * asset1_std) & (
            asset1_close <= asset1_sma + exit_threshold * asset1_std) & \
                     (asset2_close >= asset2_sma - exit_threshold * asset2_std) & (
                             asset2_close <= asset2_sma + exit_threshold * asset2_std)
    signals[exit_condition] = 0

    return signals


def calculate_daily_returns(asset1, asset2, signals, column):
    asset1_close = frames[asset1][column]
    asset2_close = frames[asset2][column]

    # Ensure all variables are Pandas Series or DataFrames
    signals = pd.Series(signals, index=asset1_close.index)  # Convert signals to a Pandas Series
    asset1_returns = asset1_close.pct_change().shift(-1)
    asset2_returns = asset2_close.pct_change().shift(-1)
    daily_returns = signals * (asset1_returns - asset2_returns)
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


def backtest(asset1, asset2, column):
    signals = entry_exit_conditions(asset1, asset2, entry_threshold, exit_threshold, column)
    daily_returns = calculate_daily_returns(asset1, asset2, signals, column)
    cumulative_returns = (1 + daily_returns).cumprod()
    cumulative_returns = cumulative_returns.drop(cumulative_returns.index[-1])
    overall_profit = (cumulative_returns.iloc[-1] - 1) * 100
    return overall_profit


entry_threshold = 0.6
exit_threshold = 0.5
profit_ETHBTC = backtest("btc", "eth", "Close").round(2)
print(f"BTC to ETH Overall profit: {profit_ETHBTC}%")
