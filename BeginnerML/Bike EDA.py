#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


bike = pd.read_csv('./hour.csv')
bike


# In[5]:


bike.temp.describe()


# In[6]:


bike.atemp.describe()


# In[111]:


sns.scatterplot(x='temp', y='atemp',data=bike)
plt.figure(figsize=(20,15))


# In[170]:


bike['var'] = round(((bike['temp']-bike['atemp']) ** 2), 3)
bike.head()


# In[180]:


sns.lineplot(x='dteday',y='var', palette="tab10", linewidth=2.5, data=bike)


# In[ ]:





# In[88]:


sns.scatterplot(x='dteday', y='cnt',data=bike)


# In[196]:


bike_1 = bike[bike['cnt'] >= 900]
sns.scatterplot(x='mnth', y='cnt', hue='yr', data=bike_1)


# In[ ]:





# In[94]:


sns.lmplot( x="dteday", y="weathersit", data=bike, fit_reg=False, hue='yr', legend=False)


# In[95]:


plt.figure(figsize=(10,7))
sns.barplot(x='mnth', y='casual',hue='yr', data=bike)


# In[164]:


plt.figure(figsize=(10,7))
sns.barplot(x='mnth', y='registered',hue='yr', data=bike)


# In[ ]:



# m1_t[['abnormal','fix','normal']].plot(kind='bar', width = width)
# m1_t['bad_rate'].plot(secondary_y=True)


# In[ ]:


df4 = bike.groupby("yr")['casual'].sum()
df4.plot(kind='bar', stacked='True')


# In[126]:


df4 = bike.groupby("yr")['registered'].sum()
df4.plot(kind='bar', stacked='True')


# In[96]:


plt.figure(figsize=(10,7))
sns.barplot(x='mnth', y='registered',hue='yr', data=bike)


# In[201]:


plt.figure(figsize=(10,7))
sns.barplot(x='weekday', y='registered',hue='yr', data=bike)


# In[58]:


plt.figure(figsize=(10,7))
sns.barplot(x='mnth', y='cnt',hue='yr', data=bike)


# In[163]:


df4 = bike.groupby("holiday")['yr'].value_counts(normalize=True).unstack()
df4.plot(kind='bar', stacked='True')


# In[66]:


plt.figure(figsize=(10,7))
sns.barplot(x='workingday', y='cnt',hue='yr', data=bike)


# In[73]:


plt.figure(figsize=(10,7))
sns.barplot(x='hr', y='cnt',hue='yr', data=bike)


# In[75]:


plt.figure(figsize=(10,7))
sns.barplot(x='weathersit', y='cnt',hue='yr', data=bike)


# In[76]:


plt.figure(figsize=(10,7))
sns.barplot(x='season', y='cnt',hue='yr', data=bike)


# In[82]:


plt.figure(figsize=(10,7))
sns.barplot(x='season', y='cnt',hue='weathersit', data=bike)


# In[85]:


df4 = bike.groupby("yr")['weathersit'].value_counts(normalize=True).unstack()
df4.plot(kind='bar', stacked='True')


# In[ ]:





# In[120]:


plt.figure(figsize=(15,10))
cmap = sns.cubehelix_palette(dark=.2, light=1, as_cmap=True)
ax = sns.barplot(x="mnth", y="temp", hue='yr', data=bike)


# In[130]:


plt.figure(figsize=(10,))
cmap = sns.cubehelix_palette(dark=.2, light=1, as_cmap=True)
ax = sns.barplot(x="weathersit", y="temp", hue='yr', data=bike)


# In[144]:


bike1 = bike[bike['yr'] == 1].groupby('mnth').mean()
bike1


# In[145]:


#p = sns.regplot(x = bike1.temp, y = ((bike1.cnt -bike1.cnt.mean())/bike1.cnt.std()))
p = sns.regplot(x = bike1.temp, y = bike1.cnt)


# In[146]:


bike2 = bike[bike['yr'] == 0].groupby('mnth').mean()
bike2


# In[147]:


p = sns.regplot(x = bike2.temp, y = bike2.cnt)


# In[152]:


bike3 = pd.merge(bike1,bike2, on='yr',how='outer')
bike3


# In[ ]:





# In[ ]:


bike1 = bike.groupby('mnth').mean()
bike1


# In[128]:


plt.figure(figsize=(15,10))
cmap = sns.cubehelix_palette(dark=.2, light=1, as_cmap=True)
ax = sns.barplot(x="mnth", y="hum", hue='yr', data=bike)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




