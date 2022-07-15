import numpy as np
from income_and_expenses import monthly_takehome_salary, monthly_expenses

# Create monthly forecasts up to 15 years from now
forecast_months = 12 * 15

# Set your annual salary growth rate
annual_salary_growth = 0.05

# Calculate your equivalent monthly salary growth rate
monthly_salary_growth = (1 + annual_salary_growth) ** (1 / 12) - 1

# Forecast the cumulative growth of your salary
cumulative_salary_growth_forecast = np.cumprod(np.repeat(1 + monthly_salary_growth, forecast_months))

# Calculate the actual salary forecast
salary_forecast = cumulative_salary_growth_forecast * monthly_takehome_salary

# Set the annual inflation rate
annual_inflation = 0.025

# Calculate the equivalent monthly inflation rate
monthly_inflation = (1 + 0.025) ** (1 / 12) - 1

# Forecast cumulative inflation over time
cumulative_inflation_forecast = np.cumprod(np.repeat(1 + monthly_inflation, forecast_months))

# Calculate your forecasted expenses
expenses_forecast = cumulative_inflation_forecast * monthly_expenses

# Calculate your savings for each month
savings_forecast = salary_forecast - expenses_forecast

# Calculate your cumulative savings over time
cumulative_savings = np.cumsum(savings_forecast)

# Print the final cumulative savings after 15 years
final_net_worth = cumulative_savings[len(cumulative_savings) - 1]
print("Your final net worth: " + str(round(final_net_worth, 2)))