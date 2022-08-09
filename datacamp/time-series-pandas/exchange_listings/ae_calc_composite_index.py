import pandas as pd
import matplotlib.pyplot as plt

market_cap_series = pd.read_csv('../stock_data/market_cap_series.csv', parse_dates=['Date'], index_col='Date')
print(market_cap_series)

# Aggregate and print the market cap per trading day. axis=1 to sum rows
raw_index = market_cap_series.sum(axis=1)
print(raw_index)

# Normalize the aggregate market cap
index = raw_index.div(raw_index.iloc[0]).mul(100)
print(index)

index.plot(title='Market-Cap Weighted Index')
plt.show()
