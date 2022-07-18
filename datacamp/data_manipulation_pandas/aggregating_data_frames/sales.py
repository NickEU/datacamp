import numpy as np
import pandas as pd

sales = pd.read_csv("sales_subset.csv")

print("Walmart sales data:")
print(sales.head())

# For each store type, aggregate weekly_sales: get min, max, mean, and median
print("\nWeekly sales data - min, max, mean, and median:\n")
sales_stats = sales[['type', 'weekly_sales']].groupby('type').agg([np.min, np.max, np.mean, np.median])

print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
print("\nUnemployment and fuel price by store type:\n")
unemployment_fuel_stats = sales[['type', 'unemployment', 'fuel_price_usd_per_l']].groupby('type').agg(
    [np.min, np.max, np.mean, np.median])

print(unemployment_fuel_stats)

# Print mean weekly_sales by department and type; fill missing values with 0
print("\nWeekly sales by department and type:\n")
print(sales.pivot_table(index=['type'], columns=['department'], values=['weekly_sales'], fill_value=0))
