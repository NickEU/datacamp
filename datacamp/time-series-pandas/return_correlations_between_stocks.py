import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./stock_data/5_stocks.csv', index_col='Date', parse_dates=['Date'])
print(data.info())

# Calculate year-end prices
annual_prices = data.resample('A').last()

annual_returns = annual_prices.pct_change()

# Calculate and print the correlation matrix
correlations = annual_returns.corr()
print(correlations)

# Visualize the correlations as heatmap
sns.heatmap(correlations, annot=True)
plt.show()
