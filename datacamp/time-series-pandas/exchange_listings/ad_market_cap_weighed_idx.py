import pandas as pd
import matplotlib.pyplot as plt

components = pd.read_csv('../stock_data/components.csv', index_col='Stock Symbol')
print(components)
stock_prices = pd.read_csv('../stock_data/stocks_4.csv', parse_dates=['Date'], index_col='Date')
print(stock_prices)

no_shares = components['Number of Shares']
print(no_shares.sort_values())
market_cap = stock_prices * no_shares
print(market_cap)

# Plot first and last market over a time period
first_value = market_cap.iloc[0]
last_value = market_cap.iloc[-1]

pd.concat([first_value, last_value], axis=1).plot(kind='barh')
plt.show()
