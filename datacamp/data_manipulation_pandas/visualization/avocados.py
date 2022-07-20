import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_csv('avocados.csv')


def most_popular_avocado_size():
    # Get the total number of avocados sold of each size
    nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()
    # Create a bar plot of the number of avocados sold by size
    nb_sold_by_size.plot(y='nb_sold', kind='bar')

    plt.show()


most_popular_avocado_size()


def changes_in_sales_over_time():
    # Get the total number of avocados sold on each date
    nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

    # Create a line plot of the number of avocados sold by date
    nb_sold_by_date.plot(kind='line')

    plt.show()


changes_in_sales_over_time()


def supply_and_demand():
    # Scatter plot of avg_price vs. nb_sold with title
    avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')

    plt.show()


supply_and_demand()


def prices_conventional_vs_organic():
    avocados[avocados['type'] == 'conventional']['avg_price'].hist()
    avocados[avocados['type'] == 'organic']['avg_price'].hist()

    plt.legend(['conventional', 'organic'])
    plt.show()


prices_conventional_vs_organic()
