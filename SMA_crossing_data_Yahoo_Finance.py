# Install Yahoo Finance
# This is a Pythong Notebook on Google Colab
!pip install yahoofinance

import yahoofinance as yf
profile = yf.AssetProfile('AAPL')
profile.to_csv('AAPL-profile.csv')

import pandas as pd
import numpy as np 
from datetime import datetime 
import matplotlib.pyplot as plt
%matplotlib inline

historical = yf.HistoricalPrices('AAPL', '2020-01-01', '2021-06-21')
dfs = historical.to_dfs()
df = dfs['Historical Prices']

AAPL = df
df.index = pd.to_datetime(df.index)
AAPL

Open	High	Low	Close	Adj Close	Volume
Date						
2020-01-02	74.059998	75.150002	73.797501	75.087502	74.207466	135480400
2020-01-03	74.287498	75.144997	74.125000	74.357498	73.486023	146322800
2020-01-06	73.447502	74.989998	73.187500	74.949997	74.071579	118387200
2020-01-07	74.959999	75.224998	74.370003	74.597504	73.723213	108872000
2020-01-08	74.290001	76.110001	74.290001	75.797501	74.909149	132079200
...	...	...	...	...	...	...
2021-06-14	127.820000	130.539993	127.070000	130.479996	130.479996	96906500
2021-06-15	129.940002	130.600006	129.389999	129.639999	129.639999	62746300
2021-06-16	130.369995	130.889999	128.460007	130.149994	130.149994	91815000
2021-06-17	129.800003	132.550003	129.649994	131.789993	131.789993	96721700
2021-06-18	130.710007	131.509995	130.240005	130.460007	130.460007	108787300
369 rows × 6 columns

fig1 = plt.figure(figsize=(15,10))
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('AAPL Share Price')
plt.plot(df[['Close']])
plt.grid(c='grey')
plt.xticks(rotation=45)

# Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(AAPL['Adj Close'], label='AAPL')
plt.title('Apple Adj. Close Price History')
plt.xlabel('Year')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

# Create the simple moving average with a 30 day window 
SMA30 = pd.DataFrame()
SMA30['Adj Close Price'] = AAPL['Adj Close'].rolling(window= 30).mean()
SMA30

# Create a simple moving 100 day average 
SMA100 = pd.DataFrame()
SMA100['Adj Close Price'] = AAPL['Adj Close'].rolling(window= 100).mean()
SMA100 

# Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(AAPL['Adj Close'], label = 'AAPL')
plt.plot(SMA30, label = 'SMA30')
plt.plot(SMA100, label = 'SMA100')
plt.title('Apple Adj. Close Price History')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2011')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

# Create a new data frame to store all the data
data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close']
data['SMA30']= SMA30
data['SMA100']= SMA100
data

# Create a function to signal when to buy and sell the asset/stock
def buy_sell(data):
  sigPriceBuy =[]
  sigPriceSell=[]
  flag=-1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['AAPL'][i])
        sigPriceSell.append(np.nan)
        flag =1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['AAPL'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)

  return (sigPriceBuy, sigPriceSell)

# Store the buy and sell data into a variable 
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

# Show the data
data

# Visualize the data and the strategy to buy and sell the stock
plt.figure(figsize=(12.6,4.6))
plt.plot(data['AAPL'],label = 'AAPL', alpha = 0.35)
plt.plot(data['SMA30'], label='SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label='SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title('Apple Adj. Close Price History Buy & Sell Signals')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2011')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()





