#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q.1 Write a Python program to print &quot;Hello Python&quot;?
print("Hello Python")


# In[14]:


# Q.2 Write a Python program to do arithmetical operations addition and division.?
def add(*args):
    a=0
    for i in args:
        if type(i)==int:
            a=a+i
    print(" this is addition for n nmuber")       
    return a
def div(a,b):
    return a/b
            


# In[19]:


print(add(23,45,55,43))
print(div(12,6))


# In[26]:


#Q.3 Write a Python program to find the area of a triangle?
def arrtri(a,b,c):
    s=(a+b+c)/3
    A=(s*(s-a)*(s-b)*(s-c))**0.5
    return A


# In[27]:


arrtri(12,3,54)


# In[30]:


# Q.4 Write a Python program to swap two variables?
def swap(a,b):
    temp=a
    a =b
    b=temp
    return a,b


# In[31]:


swap(23,34)


# In[32]:


# Q.5. Write a Python program to generate a random number?
import random


# In[37]:


n=int(input("enter your number"))
print("you random number geberated between 0 to",n  )
print(random.randint(0,n))


# In[ ]:




