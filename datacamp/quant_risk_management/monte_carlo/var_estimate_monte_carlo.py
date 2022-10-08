import numpy as np
from scipy.stats import norm

num_of_runs = 10000
# 1 day = 1440 minutes
total_steps = 1440
# mean asset losses
mu = np.array([[0.00048534], [-0.00042112], [-0.00074171], [-0.00056848]])
# efficient covariance matrix with daily variance
e_cov_daily_var = np.array([[0.00209328, 0.00114596, 0.00081893, 0.0010135],
                            [0.00114596, 0.00192715, 0.00097157, 0.00082012],
                            [0.00081893, 0.00097157, 0.00089666, 0.00064216],
                            [0.0010135, 0.00082012, 0.00064216, 0.00107184]])
portfolio_weights = [0.25, 0.25, 0.25, 0.25]

# Initialize daily cumulative loss for the assets, across N runs
daily_loss = np.zeros((4, num_of_runs))

# Create the Monte Carlo simulations for N runs
for n in range(num_of_runs):
    # Compute simulated path of length total_steps for correlated returns
    correlated_randomness = e_cov_daily_var @ norm.rvs(size=(4, total_steps))
    # Adjust simulated path by total_steps and mean of portfolio losses
    steps = 1 / total_steps
    minute_losses = mu * steps + correlated_randomness * np.sqrt(steps)
    daily_loss[:, n] = minute_losses.sum(axis=1)

losses = portfolio_weights @ daily_loss
print("Monte Carlo VaR_95 estimate: ", np.quantile(losses, 0.95))
