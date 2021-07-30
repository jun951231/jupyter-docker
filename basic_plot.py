#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40])
    plt.show()


# In[5]:


plot_show()


# In[6]:


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


# In[12]:


plot_two_list_show()


# In[11]:


def plot_marker():
    plt.plot(range(100))
    plt.draw()


# In[16]:


plot_marker_show()


# In[ ]:





# In[ ]:




