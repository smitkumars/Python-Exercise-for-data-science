#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df3= pd.DataFrame(np.random.randn(1000,4),columns=['a','b','c','d'])


# In[16]:


df3.head()


# In[17]:


df3.info()


# In[24]:


df3.plot.scatter(x='a',y='b',s=20,figsize=(12,3),color='red')


# In[27]:


df3['a'].plot.hist(bins=30)


# In[28]:


plt.style.use('ggplot')


# In[30]:


df3['a'].plot.hist(bins=30,alpha=0.5)


# In[32]:


df3[['a','b']].plot.box()


# In[34]:


df3['d'].plot.kde()


# In[35]:


df3['d'].plot.kde(lw=5,ls='--')


# In[36]:


df3['d'].plot.density(lw=5,ls='--')


# In[42]:


df3.ix[0:30].plot.area(alpha=0.4)
plt.legend(loc='center left',bbox_to_anchor=(1.0,0.5))


# In[ ]:





# In[ ]:




