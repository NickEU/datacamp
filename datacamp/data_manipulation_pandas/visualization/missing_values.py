import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import re

avocados_in_broken_format = open('avocados_2016.csv', 'r')
file_content = avocados_in_broken_format.read()
avocados_as_csv = re.sub(r"[^\S\r\n]+", ',', file_content)
avocados_ready_for_pandas = StringIO(avocados_as_csv)

# noinspection PyTypeChecker
# https://stackoverflow.com/questions/68787744/pycharm-type-checker-expected-type-none-got-str-instead-when-using-pandas-d
avocados = pd.read_csv(avocados_ready_for_pandas)

# Check individual values for missing values
print(avocados.isna())

# Check each column for missing values
print(avocados.isna().any())

# Bar plot of missing values by variable
avocados.isna().sum().plot(kind='bar')
plt.show()

# Remove rows with missing values
avocados_complete = avocados.dropna()

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
print(avocados.head())
# Create histograms showing the distributions cols_with_missing
avocados[cols_with_missing].hist()
plt.show()
