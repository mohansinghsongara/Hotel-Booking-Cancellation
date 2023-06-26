#!/usr/bin/env python
# coding: utf-8

# # importing libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading dataset
# 

# In[2]:


df = pd.read_csv('hotel_bookings 2.csv')


# In[3]:


df


# # EDA and Data Cleaning

# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df['reservation_status_date '] = pd.to_datetime(df['reservation_status_date'])


# In[10]:


df.info()


# In[11]:


df.describe(include = 'object')


# In[12]:


for col in df.describe(include= 'object').columns:
      print(col)
      print(df[col].unique())
      print('-'*50)


# In[13]:


df.isnull().sum()


# In[14]:


df.drop(['company','agent'],axis =1,inplace = True)
df.dropna(inplace = True)


# In[15]:


df.isnull().sum()


# In[16]:


df.describe()


# In[17]:


df['adr'].plot(kind = 'box')


# In[18]:


df = df[df['adr']<5000]


# In[19]:


df.describe()


# # Data Analysis and Visualizations

# In[20]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor = 'k', width = 0.7)
plt.show()


# In[32]:


plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'hotel',hue = 'is_canceled',data = df,palette = 'Blues')
legend_labels,_ = ax1.get_legend_handles_labels()
# ax1.legend(bbox_to_anchor(0,0.5))
plt.title('Reservation status in different hotels',size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[22]:


resort_hotel = df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[23]:


city_hotel = df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True) 


# In[24]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[25]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel',fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[58]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))

ax1 = sns.countplot(x = 'month',hue = 'is_canceled',data = df)


# In[57]:


plt.figure(figsize = (15,10))
plt.title('ADR per month',fontsize = 30)
sns.barplot('month','adr',data = df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[60]:


cancelled_data = df[df['is_canceled']==1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.2f',labels = top_10_country.index)
plt.show()


# In[61]:


df['market_segment'].value_counts()


# In[62]:


df['market_segment'].value_counts(normalize = True)


# In[ ]:





# In[ ]:





# In[ ]:




