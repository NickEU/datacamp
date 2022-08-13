from aa_stock_returns import StockPrices
from scipy.stats import skew, kurtosis, shapiro

clean_returns = StockPrices['Returns'].dropna()
print("Calculating the third moment (skewness) of the returns distribution...")
returns_skewness = skew(clean_returns)
print(returns_skewness)

print("Calculating the excess kurtosis of the returns distribution...")
excess_kurtosis = kurtosis(clean_returns)
print(excess_kurtosis)

print("Deriving the true fourth moment of the returns distribution...")
fourth_moment = excess_kurtosis + 3
print(fourth_moment)

print("Running the Shapiro-Wilk test on the stock returns...")
shapiro_results = shapiro(clean_returns)
print("Shapiro results:", shapiro_results)

print("Extracting the p-value from the shapiro_results...")
p_value = shapiro_results.pvalue
print("P-value: ", p_value)
print("If the p-value is less than or equal to 0.05, you can safely reject the null hypothesis of normality and "
      "assume that the data are non-normally distributed.")
