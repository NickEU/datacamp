import numpy as np
from aa_stock_returns import StockPrices

print("Calculating the average daily return of the stock...")
mean_return_daily = np.mean(StockPrices['Returns'])
print(mean_return_daily)

print("Calculating the implied annualized average return...")
trading_days_in_a_year = 252
mean_return_annualized = ((1 + mean_return_daily) ** trading_days_in_a_year) - 1
print(mean_return_annualized)

print("Calculating the standard deviation of daily return of the stock...")
sigma_daily = np.std(StockPrices['Returns'])
print(sigma_daily)

print("Calculating the daily variance...")
variance_daily = sigma_daily ** 2
print(variance_daily)

print("Annualizing the standard deviation...")
sigma_annualized = sigma_daily * 252 ** 0.5
print(sigma_annualized)

print("Calculating the annualized variance...")
variance_annualized = sigma_annualized ** 2
print(variance_annualized)
