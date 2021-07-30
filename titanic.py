#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


this = pd.read_csv("data/train.csv")


# In[3]:


f, ax = plt.subplots(1, 2, figsize= (18, 8))
series = this['Survived'].value_counts()
#print(type(series))
#print(series)
series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('0.Dead vs 1.Survived')
ax[0].set_ylabel('')
ax[1].set_title('0.Dead vs 1.Survived')
sns.countplot('Survived', data=this, ax=ax[1])


# In[4]:


this['Survived'] = this['Survived'].replace(0, 'Dead').replace(1, 'Survived')
this['Port'] = this['Embarked'].replace("C", "Chellboug").replace("S", "South Hampton").replace("Q", "Queenstown")
sns.countplot(data=this, x='Port', hue='Survived')


# In[6]:


f, ax = plt.subplots(1, 2, figsize= (18, 8))
male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
ax[0].set_title('Male 0.Dead vs 1.Survived')
ax[1].set_title('Female 0.Dead vs 1.Survived')


# In[ ]:




