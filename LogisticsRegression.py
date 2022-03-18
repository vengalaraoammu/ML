#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


# In[14]:


data=pd.read_csv('C:/Users/DELL/Desktop/DATA/CodeinGrad/ML/Iris.csv')
data


# In[15]:


data.describe()


# In[27]:


data.info()


# In[28]:


features=data.iloc[:,:-1].values
labels = data.iloc[:,-1].values


# In[32]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels,
    test_size=0.2
)


# In[36]:


lg=LogisticRegression()
lg.fit(X_train, y_train)


# In[37]:


y_pred=lg.predict(X_test)


# In[38]:


from sklearn.metrics import accuracy_score,classification_report

print(accuracy_score(y_test,y_pred))
print(classification_report(y_pred,y_test))


# In[39]:


from matplotlib import pyplot as plt


# In[91]:


plt.plot(y_pred, c='r',linestyle = 'dashed')
plt.show()


# In[47]:


# E D A


# In[48]:


data


# In[49]:


data.info()


# In[50]:


data.head()


# In[51]:


data['Species'].values


# In[53]:


display(data['Species'].value_counts())


# In[59]:


Species=data['Species'].value_counts().head(3).values
code=data['Species'].value_counts().head(3).index
plt.gcf().set_size_inches(6,6)
plt.pie(Species,labels=code,autopct="%1.1f%%",wedgeprops={'edgecolor':'black'},explode=[0.1,0,0])
plt.show()


# In[60]:


data.head()


# In[61]:


display(data['SepalLengthCm'].value_counts())


# In[64]:


Species=data['SepalLengthCm'].value_counts().head(10).values
code=data['SepalLengthCm'].value_counts().head(10).index
plt.gcf().set_size_inches(6,6)
plt.pie(Species,labels=code,autopct="%1.1f%%",wedgeprops={'edgecolor':'black'},explode=[0.1,0,0,0,0,0,0,0,0,0])
plt.title('top 10 SepalLengthCm')
plt.show()


# In[71]:


data.head()


# In[76]:


d1=data[data.Species=='Iris-setosa']


# In[83]:


plt.bar(d1['SepalLengthCm'],d1['SepalWidthCm'])
plt.title("Species")
plt.gcf().set_size_inches(5,5)
plt.xticks(rotation=90)
plt.show()


# In[82]:


plt.bar(d1['PetalLengthCm'],d1['PetalWidthCm'])
plt.title("Species")
plt.gcf().set_size_inches(5,5)
plt.xticks(rotation=90)
plt.show()


# In[84]:


plt.barh(d1['PetalLengthCm'],d1['PetalWidthCm'])
plt.title("Species")
plt.gcf().set_size_inches(5,5)
plt.xticks(rotation=90)
plt.show()


# In[90]:


plt.scatter(d1['PetalLengthCm'],d1['PetalWidthCm'])
plt.title("Species")
plt.gcf().set_size_inches(5,5)
plt.xticks(rotation=90)
plt.show()


# In[92]:


data.head()


# In[96]:


display(data['SepalLengthCm'].value_counts(),data['SepalWidthCm'].value_counts())


# In[106]:


Species=data['SepalLengthCm'].value_counts().head(10).values
code=data['SepalWidthCm'].value_counts().head(10).values
plt.plot(Species,marker = '*')
plt.plot(code, c="g",marker = 'o',mec='w',mfc='m')
plt.title('top 10 SepalLengthCm , SepalWidthCm')
plt.show()


# In[ ]:




