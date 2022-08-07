from largest_market_cap_per_sector import tickers
import pandas as pd
import matplotlib.pyplot as plt

print(tickers)
stock_prices = pd.read_csv('../stock_data/stock_data.csv', parse_dates=['Date'], index_col='Date')
print(stock_prices)

price_return = stock_prices.iloc[-1].div(stock_prices.iloc[0]).sub(1).mul(100)
print(price_return)

price_return.sort_values(ascending=False).plot(kind='barh', title='Stock Price Returns')
plt.show()
