#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[2]:


from scipy import stats
from plotly import tools
import plotly.figure_factory as ff
import plotly.tools as tls
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import warnings
warnings.filterwarnings("ignore")

# plt.style.available
plt.style.use("seaborn-whitegrid")


# In[3]:


# reading the data from local file
df = pd.read_csv(r'C:\Users\Sagar Sen\Desktop\stocks.csv')
df.head()


# In[4]:


# Lets see a brief description about our dataset
df.describe()


# In[5]:


# Replace the column name from name to ticks
# Meaning from company name to Ticks which will have all name(Apple,Amazon,etc)
df = df.rename(columns={'Name': 'Ticks'})


# In[6]:


# Let's analyze some of the stocks.(AMAZON)
amzn = df.loc[df['Ticks'] == 'AMZN']
amzn.head()


# In[7]:


amzn.info()


# In[8]:


amzn.head()


# In[9]:


# Create a copy to avoid the SettingWarning .loc issue 
amzn_df = amzn.copy()
# Change to datetime datatype.
amzn_df.loc[:, 'date'] = pd.to_datetime(amzn.loc[:,'date'], format="%Y/%m/%d")


# In[10]:


amzn_df.info()


# In[11]:


# Simple plotting of Amazon Stock Price
# First Subplot
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
ax1.plot(amzn_df["date"], amzn_df["close"])
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Stock Price")
ax1.set_title("Amazon Close Price History")

# Second Subplot
ax1.plot(amzn_df["date"], amzn_df["high"], color="green")
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Stock Price")
ax1.set_title("Amazon High Price History")

# Third Subplot
ax1.plot(amzn_df["date"], amzn_df["low"], color="red")
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Stock Price")
ax1.set_title("Amazon Low Price History")

# Fourth Subplot
ax2.plot(amzn_df["date"], amzn_df["volume"], color="orange")
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Stock Price")
ax2.set_title("Amazon's Volume History")
plt.show()


# In[ ]:




