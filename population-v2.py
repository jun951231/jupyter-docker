#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np


# In[4]:


data: [] = list()
home: [] = list()
away: object = None
result_name: str = ''


# In[6]:


#df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands=',', index_col = 0)
#df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
data = csv.reader(open('./data/202106_202106_population.csv', 'rt', encoding='UTF-8'))
next(data)
data = list(data)


# In[8]:


#print(data)


# In[10]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[11]:


plt.style.use('ggplot')
plt.plot(arr)


# In[12]:


[home.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print(home)


# In[18]:


plt.title('Pildong Population')
plt.plot(arr)


# In[22]:


mn = 1
result = 0
home = []
result_name = ''
for i in data:
    if '필동' in i[0]:
        foo = np.array(i[3:], dtype=int)/int(i[2])

home = foo
away = None
for i in data:
    bar = np.array(i[3:], dtype=int) / int(i[2])
    s = np.sum((home - bar) ** 2)
    if s < mn and '필동' not in i[0]:
        mn = s
        result_name = i[0]
        result = bar
away = result


# In[23]:


plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title('Similar to Pildong')
plt.plot(home, label='Pildong')
plt.plot(away, label='Similar to Pildong')
plt.legend()


# In[ ]:




