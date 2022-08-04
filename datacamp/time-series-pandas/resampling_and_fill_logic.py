import pandas as pd

start = '2016-1-1'
end = '2016-2-29'

# Create DateTimeIndex
monthly_dates = pd.date_range(start=start, end=end, freq='M')

monthly = pd.Series(data=[1, 2], index=monthly_dates)
print(monthly)

weekly_dates = pd.date_range(start=start, end=end, freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))
print(monthly.reindex(weekly_dates, method='bfill'))
print(monthly.reindex(weekly_dates, method='ffill'))
