def compound_interest(initial_investment, growth_periods, growth_rate, compound_periods):
    investment = initial_investment * (1 + growth_rate / compound_periods) ** (compound_periods * growth_periods)
    return investment


def compound_interest_example():
    initial_investment = 100
    growth_periods = 30
    growth_rate = 0.06
    compound_periods = 1
    # Calculate the value for the investment compounded once per year
    investment_with_interest = compound_interest(initial_investment, growth_periods, growth_rate, compound_periods)
    print("Investment 1: " + str(round(investment_with_interest, 2)))


compound_interest_example()
