import pandas as pd
import matplotlib.pyplot as plt


stocks = pd.read_csv('./stock_data/nyse.csv', parse_dates=['date'], index_col='date')
dow_jones = pd.read_csv('./stock_data/dow_jones.csv', parse_dates=['date'], index_col='date')

data = pd.concat([stocks, dow_jones], axis=1)
print(data.info())

# Normalize and plot data
first_entries = data.iloc[0]
data.div(first_entries).mul(100).plot()

plt.show()
