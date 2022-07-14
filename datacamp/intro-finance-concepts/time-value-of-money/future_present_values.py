import numpy_financial as npf

print("\nCALCULATING PRESENT VALUES\n")

# Calculate investment_1
investment_1 = npf.pv(rate=0.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=0.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")


print("\nCALCULATING FUTURE VALUES\n")


# It is important to note that in this function call, you must pass a negative value into the pv parameter
# if it represents a negative cash flow (cash going out).
# In other words, if you were to compute the future value of an investment, requiring an up-front cash payment,
# you would need to pass a negative value to the pv parameter in the .fv() function.

# Calculate investment_1
investment_1 = npf.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = npf.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")


print("\nADJUSTING FUTURE VALUES FOR INFLATION\n")


# Calculate investment_1
investment_1 = npf.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = npf.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $"
      + str(round(-investment_1_discounted, 2)) + " in today's dollars")
