import numpy as np
import numpy_financial as npf

inflation = 0.03
# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250, 100, 200, 300, 400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250, 300, -250, 300, 300])

# Calculate the net present value of project 1
investment_1 = npf.npv(rate=inflation, values=cash_flows_1)
print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = npf.npv(rate=inflation, values=cash_flows_2)
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")

# Remember how compounded returns grow rapidly over time? Well, it works in the reverse, too.
# Compounded discount factors over time will quickly shrink a number towards zero.

# Calculate investment_1
future_value = 100

investment_1 = npf.pv(rate=inflation, nper=30, pmt=0, fv=future_value)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=inflation, nper=50, pmt=0, fv=future_value)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = npf.pv(rate=inflation, nper=100, pmt=0, fv=future_value)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")

# This means that the longer in the future your cash flows will be received (or paid),
# the closer to 0 that number will be.
