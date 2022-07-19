import pandas as pd

temperatures = pd.read_csv("temperatures.csv")

# Add a year column to temperatures
temperatures['year'] = pd.to_datetime(temperatures['date']).dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = pd.pivot_table(temperatures, 'avg_temp_c', index=['country', 'city'], columns=['year'])

print("\nAvg temp by country and city for each year:\n")
print(temp_by_country_city_vs_year)

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), '2005':'2010'])

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
print("\nWorldwide mean temp by year:\n")
print(mean_temp_by_year)

print("\nYear with the highest mean temp:\n")
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

print("\nCity with the lowest mean temp:\n")
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
