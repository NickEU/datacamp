import pandas as pd
import matplotlib.pyplot as plt

# Import data here
prices = pd.read_csv("./stock_data/asset_classes.csv", parse_dates=['DATE'], index_col='DATE')

# Inspect prices here
print(prices.info())

# Select first prices
first_prices = prices.iloc[0]

# Create normalized
normalized = prices / first_prices * 100

# Plot normalized
normalized.plot()
plt.show()
