#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df= pd.read_csv(r"C:\Users\DELL\Desktop\Clean_Dataset.csv")


# In[3]:


print(df)


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.isnull()


# In[7]:


df.isnull().sum()


# In[8]:


#Basic information

df.info()


# In[9]:



#Describe the data

df.describe()


# In[10]:


import matplotlib.pyplot as plt

plt.hist(df['price'], bins=50)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# In[11]:


plt.scatter(df['duration'], df['price'])
plt.xlabel('Duration (hours)')
plt.ylabel('Price')
plt.show()


# In[12]:


print(df['price'].describe())


# In[13]:


from scipy.stats import zscore

z_scores = zscore(df['price'])
for i, z_score in enumerate(z_scores):
    if abs(z_score) > 3:
        print(f"Outlier detected at index {i}")


# In[ ]:




