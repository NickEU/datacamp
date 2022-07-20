import pandas as pd
import matplotlib.pyplot as plt

# Create tickers
tickers = ['MSFT', 'AAPL']

stocks = pd.read_csv('./stock_data/msft_aapl.csv', parse_dates=['date'], index_col='date')
sp500 = pd.read_csv('./stock_data/sp500.csv', parse_dates=['date'], index_col='date')
print(sp500.head())
# Concatenate stocks and index
data = pd.concat([stocks, sp500], axis=1).dropna()
print(data.head())
# Normalize data
normalized = data.div(data.iloc[0]).mul(100)
print(normalized['SP500'].head())
# Subtract the normalized index from the normalized stock prices, and plot the result
perf_vs_bench_idx = normalized[tickers].sub(normalized['SP500'], axis=0).plot()
plt.show()
