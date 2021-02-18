#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import pandas_profiling
import warnings
warnings.filterwarnings('ignore')


# In[ ]:





# In[9]:


HEART = pd.read_csv('D:\heart.csv')


# In[10]:


HEART.head()


# In[11]:


HEART.shape


# In[12]:


HEART.dtypes


# In[13]:


HEART.age.value_counts()


# In[14]:


HEART_edad = HEART[HEART.age == 65]


# In[15]:


HEART_edad.reset_index(drop=True, inplace=True)


# In[16]:


HEART_edad.shape


# In[17]:


HEART.dtypes


# In[18]:


HEART.head()


# In[20]:


HEART.head()


# In[21]:


HEART.shape


# In[22]:


HEART.dtypes


# In[28]:


HEART_edad.profile_report()


# In[ ]:




