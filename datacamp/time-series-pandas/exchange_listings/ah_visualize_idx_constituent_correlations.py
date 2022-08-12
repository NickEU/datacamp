import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stock_prices = pd.read_csv('../stock_data/stock_data.csv', parse_dates=['Date'], index_col='Date')


def visualize_constituent_correlations():
    print(stock_prices.info())

    daily_returns = stock_prices.pct_change()

    # Calculate and print the pairwise correlations
    correlations = daily_returns.corr()
    print(correlations)

    sns.heatmap(correlations, annot=True)
    plt.title('Daily Return Correlations')
    plt.show()


def save_returns_to_excel():
    index_series = pd.read_csv('../stock_data/index.csv', parse_dates=['Date'], index_col='Date').squeeze()
    index_series.rename('Index', inplace=True)
    print(index_series.info())
    print(stock_prices.info())

    data = stock_prices.join(index_series)
    print(data.info())

    idx_and_stock_returns = data.pct_change()

    with pd.ExcelWriter('data.xls') as writer:
        data.to_excel(writer, sheet_name='data')
        idx_and_stock_returns.to_excel(writer, sheet_name='returns')


visualize_constituent_correlations()
save_returns_to_excel()
