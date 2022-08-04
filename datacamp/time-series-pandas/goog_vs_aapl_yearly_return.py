import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./stock_data/apple_google.csv', parse_dates=['Date'], index_col='Date')


def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1


daily_returns = data.pct_change()

rolling_annual_returns = daily_returns.rolling('360D').apply(multi_period_return)

rolling_annual_returns.mul(100).plot()
plt.show()
