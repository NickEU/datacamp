import pandas as pd
import matplotlib.pyplot as plt

monthly = pd.read_csv("./stock_data/unrate.csv", parse_dates=['DATE'], index_col='DATE')
print(monthly.info())

weekly_dates = pd.date_range(start=monthly.index.min(), end=monthly.index.max(), freq='W')

weekly = monthly.reindex(weekly_dates)

weekly['ffill'] = weekly['UNRATE'].ffill()
print(weekly)
print(weekly.resample('W').interpolate())
weekly['interpolated'] = weekly['UNRATE'].resample('W').interpolate()

weekly.plot()
plt.show()


def interpolate_debt_gdp_compare_to_unrate():
    # Import & inspect data here
    data = pd.read_csv('./stock_data/debt_unemployment.csv', parse_dates=['date'], index_col='date')
    print(data.info())

    # Interpolate and inspect here
    interpolated = data.interpolate()
    print(interpolated.info())

    # Plot interpolated data here
    interpolated.plot(secondary_y='Unemployment')
    plt.show()


interpolate_debt_gdp_compare_to_unrate()


def compare_stock_prices_ggl_fb():
    # Import and inspect data here
    stocks = pd.read_csv('./stock_data/goog_fb.csv', parse_dates=['date'], index_col='date')
    print(stocks.info())
    # Calculate and plot the monthly averages
    monthly_average = stocks.resample('M').mean()
    monthly_average.plot(subplots=True)
    plt.show()


compare_stock_prices_ggl_fb()
