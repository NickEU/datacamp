import pandas as pd
import matplotlib.pyplot as plt

air_quality_nyc = pd.read_csv('./air_quality/ozone_nyc.csv', parse_dates=['date'], index_col='date')

air_quality_nyc = air_quality_nyc.resample('D').interpolate()
print(air_quality_nyc.info())


# Create the rolling window
rolling = air_quality_nyc.Ozone.rolling(window=360)

# Insert the rolling quantiles to the monthly returns
air_quality_nyc['q10'] = rolling.quantile(0.1)
air_quality_nyc['q50'] = rolling.quantile(0.5)
air_quality_nyc['q90'] = rolling.quantile(0.9)

air_quality_nyc.plot()
plt.show()
