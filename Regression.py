#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[57]:


x=[i for i in range(1,8)]
y=[1.7, 3.2, 5.6, 8.0, 12.2, 13.3, 15]

data=pd.DataFrame(
    data={
        "X":x,
        "Y":y,
        
    }
)


# $$ m = \frac{n\sum x*y - \sum x\sum y}{n\sum x^{2} - (\sum x)^{2}} $$

# In[58]:


data


# In[59]:


data['XY'] = data['X'] * data['Y']
data["X^2"]=data['X'] ** 2


# In[60]:


data


# In[61]:


d=len(data)
Sum_xy= data["XY"].sum()
sum_x= data["X"].sum()
sum_y= data["Y"].sum()
sum_x_2= data["X^2"].sum()
sum_X_h_2= sum_x ** 2


# In[62]:


print(d, Sum_xy, sum_x, sum_y, sum_x_2, sum_X_h_2)


# In[63]:


numerator_m=(n*(Sum_xy)) - (sum_x * sum_y)
dinominator_m=(n*(sum_x_2)-(sum_X_h_2))


# In[64]:


m=numerator_m/dinominator_m


# In[65]:


m


# $$b = \frac{\sum y - m * \sum x}{n}$$

# In[66]:


numerator_b = sum_y - (m * sum_x)
denominator_b = len(data)


# In[67]:


b=numerator_b/denominator_b


# In[68]:


b


# $$y_{pred} = m\sum_{i = 1}^{n}X + b $$

# In[73]:


y_pred=[round((m* Xi + b),2) for Xi in data['X']]
y_pred


# $$squarederror = \sum_{i=0}^{n}  (y_{pred} - y_{org})^{2}$$

# In[70]:


squared_error = sum([(y_pred_value - y_org_value) ** 2 
                for y_pred_value, y_org_value in zip(y_pred, data['Y'].values)])
squared_error


# In[72]:


import matplotlib.pyplot as plt

plt.scatter(list(range(len(data))), data['Y'].values, label="original")
plt.plot(list(range(len(data))), y_pred, c='r', label="predicted")
plt.scatter(list(range(len(data))), y_pred, c='y', label="predicted_S")

plt.legend()
plt.show()


# In[ ]:


class Logistic:
    def __init__(self,data):
        self.n = len(data)
        self.sum_xy = data['XY'].sum()
        self.sum_x = data['X'].sum()
        self.sum_y = data['Y'].sum()
        self.sum_x_2 = data['X^2'].sum()
        self.sum_x_h_2 = sum_x ** 2
        
        pass
    
    def m_value(self):
        numerator_m=(n*(Sum_xy)) - (sum_x * sum_y)
        dinominator_m=(n*(sum_x_2)-(sum_X_h_2))
        
        m = numerator_m / denominator_m
        
        pass
    
    def b_values(self):
        
        numerator_b = sum_y - (m * sum_x)
        denominator_b = len(data)
        
        b=numeratoe_b/denominator_b
        
        pass
    
    def final_value(self):
        
        y_pred=[round((m* Xi + b),2) for Xi in data['X']]
            
            pass
        
    def squared(self):
        squared_error = sum([(y_pred_value - y_org_value) ** 2 
                for y_pred_value, y_org_value in zip(y_pred, data['Y'].values)])
        
            pass
        
        


# In[88]:


a=[i for i in range(1,8)]
b=[1.7, 3.2, 5.6, 8.0, 12.2, 13.3, 15]

d=data(a,b)


# In[ ]:




