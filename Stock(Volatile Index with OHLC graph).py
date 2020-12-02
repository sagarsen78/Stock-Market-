#!/usr/bin/env python
# coding: utf-8

# In[18]:


print('hello world')


# In[21]:


#importing library functions
import pandas as pd

#reading the .csv file from local machine
datafile = r'C:\Users\Sagar Sen\Desktop\stocks.csv'
data = pd.read_csv(datafile, index_col = 'date')
data.index = pd.to_datetime(data.index) # Converting the dates from string to datetime format

#showing output of the CSV file
data


# In[22]:


#importing the mpl finance library
import mplfinance as mpf


# In[31]:


# We need to exctract the OHLC prices into a list of lists:
dvalues = data[['open', 'high', 'low', 'close']].values.tolist()

# Dates in our index column are in datetime format, we need to comvert them 
# to Matplotlib date format (see https://matplotlib.org/3.1.1/api/dates_api.html):
pdates = mdates.date2num(data.index)

# If dates in our index column are strings instead of datetime objects, we should use:
# pdates = mpl.dates.datestr2num(data.index)

# We prepare a list of lists where each single list is a [date, open, high, low, close] sequence:
ohlc = [ [pdates[i]] + dvalues[i] for i in range(len(pdates)) ]


#     We can now use the data to plot a bar chart

# In[35]:


import mpl_finance as mpf # This is the old mpl-finance library - note the '_' in the library name

# We can now feed the ohlc matrix into mpl-finance to create a candle stick chart:

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize = (12,6))

mpf.plot_day_summary_ohlc(ax, ohlc[-50:], ticksize = 5)

ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('S&P 500-Bar Chart')

# Choosing to display the dates as "Month Day":
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# This is to automatically arrange the date labels in a readable way:
fig.autofmt_xdate()

#NOTE- the below is the last 50 days stocks displayed


# In[33]:


# Most and least volatile stocks 


# In[ ]:





# In[ ]:




