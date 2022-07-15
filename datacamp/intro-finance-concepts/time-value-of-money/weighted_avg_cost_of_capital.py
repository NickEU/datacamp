import numpy_financial as npf
from internal_rate_of_return import cf_project1, cf_project2

# Set the market value of debt
mval_debt = 1000000

# Set the market value of equity
mval_equity = 1000000

# Compute the total market value of your company's financing
mval_total = mval_debt + mval_equity

# Compute the proportion of your company's financing via debt
percent_debt = mval_debt / mval_total
print("Debt Financing: " + str(round(100 * percent_debt, 2)) + "%")

# Compute the proportion of your company's financing via equity
percent_equity = mval_equity / mval_total
print("Equity Financing: " + str(round(100 * percent_equity, 2)) + "%")

# Assume a cost of equity of 18% based on similar companies.
cost_equity = 0.18
# The bank is willing to lend at an interest rate of 12%.
cost_debt = 0.12
# Assume a corporate tax rate of 35% and that your debt financing is tax-deductible.
tax_rate = 0.35

# Calculate the WACC
wacc = cost_equity * percent_equity + cost_debt * percent_debt * (1 - tax_rate)
print("WACC: " + str(round(100 * wacc, 2)) + "%")


# Calculate the net present value for Project 1
npv_project1 = npf.npv(wacc, cf_project1)
print("Project 1 NPV: " + str(round(npv_project1, 2)))

# Calculate the net present value for Project 2
npv_project2 = npf.npv(wacc, cf_project2)
print("Project 2 NPV: " + str(round(npv_project2, 2)))