#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ASSIGNMENT


# In[ ]:


#PROBLEM 1


# In[ ]:


Write a python program to removeNone value from a given list. ( using list comprension)


# In[3]:


given_list=[12,0,None,23,None,-55,234,89,None,0,6,-12]
new_list=[x for x in given_list if x is not None]
print(new_list)


# In[ ]:


#PROBLEM 2


# In[ ]:


Write a function for calculating area of square


# In[4]:


def calculate_square_area(a):
    area=a*a
    return area


# In[5]:


area=calculate_square_area(12)
print(area)


# In[ ]:


#PROBLEM 3


# In[6]:


import math


# In[7]:


def calculate_circle_area(r):
    area= math.pi * r * r
    return area
    


# In[10]:


area=calculate_circle_area(10)
print(area)


# In[ ]:




