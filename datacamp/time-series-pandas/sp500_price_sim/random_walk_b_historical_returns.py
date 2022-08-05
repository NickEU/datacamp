from numpy.random import choice, seed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fb_stock_price_history = pd.read_csv('../stock_data/fb.csv', parse_dates=[0], index_col=0,
                                     header=None, names=['date', 'price'])

daily_returns = fb_stock_price_history.pct_change().dropna()
count_observations = daily_returns.price.count()

seed(11)
random_walk = choice(daily_returns.price, count_observations)

random_walk = pd.Series(random_walk)

# Plot random_walk distribution
if __name__ == "__main__":
    sns.histplot(random_walk, kde=True, stat="density", linewidth=0)
    plt.show()
