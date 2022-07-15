import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as npf
from savings_expenses_salary_forecasts import salary_forecast, expenses_forecast, forecast_months

# Set the annual investment return to 7%
investment_rate_annual = 0.07

# Calculate the monthly investment return
investment_rate_monthly = (1 + investment_rate_annual) ** (1 / 12) - 1

# Calculate your required monthly investment to amass $1M
required_investment_monthly = -1 * npf.pmt(rate=investment_rate_monthly, nper=12 * 15, pv=0, fv=1000000)
print(
    "You will have to invest $" + str(round(required_investment_monthly, 2)) + " per month to amass $1M over 15 years")

cash_flow_forecast = salary_forecast - expenses_forecast
monthly_investment_percentage = 0.30

# Calculate your monthly deposit into your investment account
investment_deposit_forecast = cash_flow_forecast * monthly_investment_percentage

# The rest goes into your savings account
savings_forecast_new = cash_flow_forecast * (1 - monthly_investment_percentage)

# Calculate your cumulative savings over time
cumulative_savings_new = np.cumsum(savings_forecast_new)
investment_portfolio = np.zeros(forecast_months, dtype=np.int64)
net_worths = np.zeros(forecast_months, dtype=np.int64)
# Loop through each forecast period
for i in range(forecast_months):

    # Find the previous investment deposit amount
    if i == 0:
        previous_investment = 0
    else:
        previous_investment = investment_portfolio[i - 1]

    # Calculate the value of your previous investments, which have grown
    previous_investment_growth = previous_investment * (1 + investment_rate_monthly)

    # Add your new deposit to your investment portfolio
    investment_portfolio[i] = previous_investment_growth + investment_deposit_forecast[i]

    # Calculate your net worth at each point in time
    net_worths[i] = investment_portfolio[i] + cumulative_savings_new[i]


# Plot your forecasted cumulative savings vs investments and net worth
def plot_investments(investments, savings, net_worth):
    plt.plot(investments, color='red', label='Investments')
    plt.plot(savings, color='blue', label='Savings')
    plt.plot(net_worth, color='green', label='Net Worth')
    plt.legend(loc="upper left")
    plt.show()


plot_investments(investment_portfolio, cumulative_savings_new, net_worths)




