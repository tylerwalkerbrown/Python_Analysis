#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas_datareader.data as web
import pandas as pd
import datetime
import tweepy
from textblob import TextBlob
import re
import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY


# In[91]:


start = datetime.datetime(2020,1,1)
end = datetime.datetime(2022,2,15)


# In[124]:


Tesla = web.DataReader("TSLA", 'yahoo', start, end )
Bitcoin = web.DataReader("GALA-USD", 'yahoo', start, end )


# In[125]:


Bitcoin.head
Tesla.head


# In[126]:


Tesla['Open'].plot(label = 'TSLA Open price' )
Tesla['Close'].plot(label = 'TSLA Close price' )
Bitcoin['Open'].plot(label = 'Bitcoin price')
Bitcoin['Close'].plot(label = 'Bitcoin Low price')
plt.yscale("log")
plt.legend()
plt.ylabel('Stock Price')
plt.show()


# In[127]:


Tesla['Volume'].plot.hist(bins = 40)
plt.show()


# In[128]:


Tesla['Volume'].plot()
plt.show()
Bitcoin['Volume'].plot()
plt.show()


# In[129]:


Tesla['Open'].plot()
plt.show()
Bitcoin['Open'].plot()
plt.show()


# In[130]:


Bitcoin['Volume'].plot(label='BTC-USD',figsize=(15,7))
Tesla['Volume'].plot(label='Tesla')
plt.ylabel('Volume')
plt.legend()
plt.show()

Bitcoin.iloc[400:500].plot()


# In[131]:


Tesla['Total Traded']= Tesla['Open'] * Tesla['Volume']
Bitcoin['Total Traded']= Bitcoin['Open'] * Bitcoin['Volume']
Tesla.head()
Bitcoin.head()


# In[132]:


Tesla['Total Traded'].plot(label= 'Tesla')


# In[133]:


Bitcoin['Total Traded'].plot(label = 'Bitcoin')


# In[134]:


Tesla['Total Traded'].plot(label= 'Tesla')
Bitcoin['Total Traded'].plot(label = 'Bitcoin', figsize = (15,7))
plt.ylabel('Total Traded')
plt.legend()
plt.show()


# In[135]:


Bitcoin.iloc[[Bitcoin['Total Traded'].argmax()]]


# In[136]:


Tesla.iloc[[Tesla['Total Traded'].argmax()]]


# In[137]:


Bitcoin['Total Traded'].argmax()


# In[138]:


Tesla['Open'].plot(figsize = (15,7))


# In[139]:


Bitcoin['Open'].plot(figsize = (15,7))
Bitcoin['MA50'] = Bitcoin['Open'].rolling(100).mean()
Bitcoin['MA50'].plot(label = 'MA50')
plt.legend()


# In[140]:


comp = pd.concat([Tesla['Open'], Bitcoin['Open']], axis = 1)
comp.columns= ['Tesla Open', 'Bitcoin Open']


# In[141]:


scatter_matrix(comp, figsize = (8,8), hist_kwds = {'bins': 50} )


# In[142]:


TeslaReset = Tesla.loc['2012-01':'2012-01'].reset_index()
TeslaReset['date_ax'] = TeslaReset['Date'].apply(lambda date: date2num(date))
Tesla_values = [tuple(vals) for vals in TeslaReset[['date_ax', 'Open', 'High', 'Low', 'Close']].values]

mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

fig, ax = plt.subplots()
candlestick_ohlc(ax, Tesla_values, width = 0.6, colorup = 'g', colordown = 'r' )


# In[143]:


Tesla['returns'] = (Tesla['Close']/Tesla['Close'].shift(1)) - 1


# In[144]:


Bitcoin['returns'] = (Bitcoin['Close']/Bitcoin['Close'].shift(1)) - 1


# In[145]:


Tesla['returns'].hist(bins=50)


# In[146]:


Bitcoin['returns'].hist(bins=50)


# In[147]:


Bitcoin['returns'].hist(bins=50, alpha = .2, figsize = (13,6), label = 'Bitcoin')
Tesla['returns'].hist(bins=50, alpha = .2, label = 'Tesla')
plt.legend()


# In[148]:


Bitcoin['returns'].plot( label = 'Bitcoin')


# In[149]:


Tesla['returns'].plot(label = 'Tesla')


# In[150]:


Bitcoin['returns'].plot( label = 'Bitcoin')
Tesla['returns'].plot(label = 'Tesla')
plt.legend()


# In[151]:


box_df = pd.concat([Tesla['returns'], Bitcoin['returns']], axis = 1)
box_df.columns=['Tesla Returns', 'Bitcoin Returns']
box_df.plot(kind= "box", figsize = (16,6))


# In[152]:


scatter_matrix(box_df, figsize = (8,8), hist_kwds = {'bins':50}, alpha = 0.3)


# In[153]:


Tesla['Cumulative Return'] = (1+ Tesla['returns']).cumprod()
Bitcoin['Cumulative Return'] = (1+ Bitcoin['returns']).cumprod()


# In[154]:


Tesla['Cumulative Return']. plot(label = 'Tesla' , figsize = (15,7))
Bitcoin['Cumulative Return'].plot(label = "Bitcoin")
plt.legend()


# In[ ]:





# In[ ]:




