import pandas as pd
import matplotlib.pyplot as plt

sp500 = pd.read_csv('./stock_data/sp500.csv', parse_dates=['date'], index_col='date')
print(sp500.info())

# Calculate daily returns
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean', 'median', 'std'])

stats.plot()
plt.show()

