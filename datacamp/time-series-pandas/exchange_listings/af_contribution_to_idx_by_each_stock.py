import pandas as pd
import matplotlib.pyplot as plt

index = pd.read_csv('../stock_data/index.csv', parse_dates=['Date'], index_col='Date').squeeze()
components = pd.read_csv('../stock_data/components.csv', index_col='Stock Symbol')

# Calculate and print the index return
index_return = (index[-1] / index[0] - 1) * 100
print(index_return)

market_cap = components['Market Capitalization']
total_market_cap = market_cap.sum()

# Calculate the index component weights
weights = market_cap.div(total_market_cap)
print(weights.sort_values())

# Calculate and plot the contribution by component
weights.mul(index_return).sort_values().plot(kind='barh')
plt.show()
