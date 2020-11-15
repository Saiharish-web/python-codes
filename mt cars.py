#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as py
from matplotlib import pyplot as plt


# In[4]:


mtcars = pd.read_csv("mtcars.csv")
mtcars


# In[5]:


mtcars.head


# In[6]:


mtcars.tail


# In[11]:


mtcars.shape


# In[9]:


mtcars.describe()


# In[12]:


pd.crosstab(mtcars.gear,mtcars.cyl)


# In[22]:


pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar")
plt.style.use ('classic')


# In[23]:


pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="hist")
plt.style.use ("classic")


# In[24]:


mtcars.gear.value_counts()


# In[27]:


mtcars.gear.value_counts().plot(kind = "pie")
plt.style.use ("classic")


# In[28]:


mtcars.gear.value_counts().plot(kind = "bar")


# In[29]:


mtcars.gear.value_counts().plot(kind = "hist")


# In[30]:


import seaborn as sns


# In[31]:


sns.boxplot(x="gear",y="mpg",data=mtcars)


# In[32]:


sns.pairplot(mtcars.iloc[:,0:4])


# In[34]:


plt.plot(mtcars.mpg,mtcars.hp,"bo")
plt.xlabel("mpg")
plt.ylabel("hp")


# In[36]:


plt.plot(mtcars.disp,mtcars.hp,"ro")
plt.xlabel("mpg")
plt.ylabel("hp")


# In[ ]:




