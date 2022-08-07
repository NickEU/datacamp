from index_comp_sector_stock_returns import exchange_listings

# Select largest company for each sector and print sorting by market cap
components = exchange_listings.groupby('Sector')['Market Capitalization'].nlargest(1)
if __name__ == "__main__":
    print(components.sort_values(ascending=False))

tickers = components.index.get_level_values('Stock Symbol')
if __name__ == "__main__":
    print(tickers)
    print(exchange_listings)

info_cols = ['Company Name', 'Market Capitalization', 'Last Sale']
largest_companies = exchange_listings.loc[tickers, info_cols].sort_values(by='Market Capitalization', ascending=False)
if __name__ == "__main__":
    print(largest_companies)
