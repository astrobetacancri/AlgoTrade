# AlgoTrade

Yahoo Finance for Python 

## Libraries 
Pandas 
Numpy 
matplotlib.pyplot

### Output
AAPL Buy Price Signal SharePrice graph with SMA 30 & 100 

![Image](/Image/BuySellSignal.png)

### Customization
1. Define Stock Ticker
```
# Define Stock Ticker HERE, then Run all
STOCK = 'arkk'
print(STOCK)


import yahoofinance as yf
profile = yf.AssetProfile(STOCK)
profile.to_csv(STOCK + '-profile.csv')

historical = yf.HistoricalPrices(STOCK, '2020-01-01', '2021-06-21')
```


