import pandas as pd
import matplotlib.pyplot as plt
from random_walk_b_historical_returns import random_walk, fb_stock_price_history, daily_returns

start_price = fb_stock_price_history.price.first('1D')

random_walk = random_walk.add(1)
random_walk.index = daily_returns.index
print(random_walk)
random_price = pd.concat([start_price, random_walk])

random_price = random_price.cumprod()

fb_stock_price_history['random'] = random_price
print(fb_stock_price_history)
fb_stock_price_history.plot()
plt.show()
