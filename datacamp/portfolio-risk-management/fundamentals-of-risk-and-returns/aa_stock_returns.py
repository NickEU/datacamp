import matplotlib.pyplot as plt
import pandas as pd

StockPrices = pd.read_csv("MSFTPrices.csv", parse_dates=['Date'], index_col='Date')
StockPrices = StockPrices.sort_values(by='Date')
print(StockPrices.head())


def calc_daily_returns():
    # Calculate the daily returns of the adjusted close price
    StockPrices['Returns'] = StockPrices['Adjusted'].pct_change()
    print(StockPrices.head())

    StockPrices['Returns'].plot()
    plt.show()


def calc_return_distributions():
    # Convert the decimal returns into percentage returns
    percent_return = StockPrices['Returns'] * 100
    returns_plot = percent_return.dropna()

    plt.hist(returns_plot, bins=75)
    plt.show()


calc_daily_returns()
calc_return_distributions()
