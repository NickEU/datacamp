import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

djia = pd.read_csv('../stock_data/djia.csv', parse_dates=['date'], index_col='date')
index = pd.read_csv('../stock_data/index.csv', parse_dates=['Date'], index_col='Date').squeeze()

data = index.to_frame('Index')
print(djia)

# Normalize djia series and add as new column to data
djia = djia / djia.iloc[0] * 100
data['DJIA'] = djia

print('Total return(in percentages) for:')
print(data.iloc[-1].div(data.iloc[0]).sub(1).mul(100))

data.plot(title="Index return vs DJIA")
plt.show()


def multi_period_return(r):
    return (np.prod(r + 1) - 1) * 100


rolling_return_360 = data.pct_change().rolling('360D').apply(multi_period_return)

rolling_return_360.plot(title="Index Rolling 360D Return vs DJIA")
plt.show()
