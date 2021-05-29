#!/usr/bin/env python
# coding: utf-8

# In[1]:



import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


sns.set_style('whitegrid')


# In[3]:


titanic = sns.load_dataset('titanic')


# In[4]:


titanic.head()


# In[5]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[8]:


sns.distplot(titanic['fare'],kde=False)


# In[13]:


sns.distplot(titanic['fare'],kde=False,color='red',bins=50)


# In[16]:


sns.boxplot(x='class',y='age',data=titanic)


# In[17]:


sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')


# In[20]:


sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')


# In[22]:


sns.countplot(x='sex',data=titanic)


# In[24]:


sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')


# In[25]:


g= sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')


# In[26]:


g= sns.FacetGrid(data=titanic,col='sex')
g.map(sns.distplot,'age')


# In[ ]:




