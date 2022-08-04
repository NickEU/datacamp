import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./stock_data/apple_google.csv', parse_dates=['Date'], index_col='Date')

investment = 1000

daily_returns = data.pct_change()

returns_plus_one = daily_returns + 1
cumulative_return = returns_plus_one.cumprod()

investment_return = cumulative_return.mul(investment).plot()
plt.show()
