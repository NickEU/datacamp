import pandas as pd
import matplotlib.pyplot as plt

gdp_growth = pd.read_csv('./stock_data/gdp_growth.csv', parse_dates=['date'], index_col='date')
print(gdp_growth.info())

djia = pd.read_csv('./stock_data/djia.csv', parse_dates=['date'], index_col='date')
print(djia.info())

djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here
data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)

data.rename(columns={'gdp_growth': 'gdp'}, inplace=True)
data.plot()
plt.show()
