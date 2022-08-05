from numpy.random import normal, seed
import pandas as pd
import matplotlib.pyplot as plt

seed(42)
# Drawing random numbers from the normal distribution
random_walk = normal(loc=.001, scale=0.01, size=2500)

random_walk = pd.Series(random_walk)

random_prices = random_walk.add(1).cumprod()

first_price = pd.Series([1000])
# Doing concat like this leads to index duplication - need to reindex first.
random_prices.index = random_prices.index + 1
random_prices = pd.concat([first_price, random_prices.mul(1000)])
random_prices.plot()
plt.show()
