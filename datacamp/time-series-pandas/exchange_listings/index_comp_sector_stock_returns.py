import pandas as pd

exchange_listings = pd.read_excel('../stock_data/listings.xlsx')
if __name__ == "__main__":
    print(exchange_listings)

exchange_listings.set_index('Stock Symbol', inplace=True)
exchange_listings.dropna(subset=['Sector'], inplace=True)

exchange_listings = exchange_listings[exchange_listings['IPO Year'] < 2019]
if __name__ == "__main__":
    print(exchange_listings.info())

    print('The number of companies per sector:')
    print(exchange_listings.groupby('Sector').size().sort_values(ascending=[False]))

