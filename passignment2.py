#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Q.1 Write a Python program to convert kilometers to miles?
def kmtm(n):
    return n*0.621371


# In[16]:


#Q.2 Write a Python program to convert Celsius to Fahrenheit?
def celtfa(n):
    return n*(1.8)+32
    


# In[18]:


celtfa(23)


# In[29]:


#Q.3 Write a Python program to display calendar?
import calendar
yy=int(input("enter year :"))

print(calendar.calendar(yy))


# In[30]:


# Q.4 Write a Python program to solve quadratic equation?
def quadeq(a,b,c):
    x=(-b+((b**2)-4*a*c)**0.5)/2*a
    y= x=(-b-((b**2)-4*a*c)**0.5)/2*a
    return x,y


# In[31]:


quadeq(1,3,2)


# In[32]:


#Q.5 Write a Python program to swap two variables without temp variable?
def swap(a,b):
    a,b=b,a
    return a,b


# In[33]:


swap(2,3)


# In[ ]:




