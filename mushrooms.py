#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as py 
from matplotlib import pyplot as plt


# In[4]:


mushrooms = pd.read_csv("mushrooms[1].csv")


# In[5]:


mushrooms


# In[7]:


mushrooms.head(5)


# In[8]:


mushrooms.tail(5)


# In[9]:


mushrooms.shape


# In[10]:


mushrooms.describe()


# In[11]:


pd.crosstab(mushrooms.bruises,mushrooms.odor)


# In[16]:


pd.crosstab(mushrooms.population,mushrooms.habitat)


# In[17]:


pd.crosstab(mushrooms.population,mushrooms.habitat).plot(kind = "bar")


# In[20]:


pd.crosstab(mushrooms.bruises,mushrooms.odor).plot(kind="bar")
plt.style.use ("bmh")


# In[21]:


mushrooms.bruises.value_counts()


# In[22]:


mushrooms.bruises.value_counts().plot(kind="pie")

mushrooms.habitat.value_counts().plot(kind="pie")
plt.style.use("bmh")
# In[24]:


mushrooms.population.value_counts().plot(kind ="bar")


# In[25]:


mushrooms.population.value_counts().plot(kind="hist")


# In[36]:


import seaborn as sns
              


# In[39]:


plt.plot(mushrooms.habitat,mushrooms.population,"bo")
plt.xlabel("habitat")
plt.ylabel("population")


# In[41]:


plt.plot(mushrooms.bruises,mushrooms.odor,"ro")
plt.xlabel("bruises")
plt.ylabel("odor")


# In[ ]:




