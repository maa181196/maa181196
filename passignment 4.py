#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q.1Write a Python Program to Find the Factorial of a Number?
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        a=1
        for i in range(1,n+1):
            a=a*i
        return a
            


# In[7]:


fact(7)


# In[24]:


# Q.2 Write a Python Program to Display the multiplication Table?
def table(n):
    a=1
    for i in range(1,11):
        a=n*i
        print(a)
    return a


# In[26]:


table(34)


# In[1]:


#Q.3 Write a Python Program to Print the Fibonacci sequence?
def fabinacci(n):
    a=1
    b=2
    l=[]
    for i in range(1,n+1):
        l.append(a)
        a,b=b,a+b
    return l
            
  
   


# In[3]:


fabinacci(12)


# In[ ]:


#Q.4 Write a Python Program to Check Armstrong Number?


# In[70]:


def armstrong(n):
    a=str(n)
    l=[]
    for i in a:
        b=int(i)
        order=len(a)
        l.append(b**order)
    d=0
    for j in l:
        d=d+j
    if d==n:
        return "nmuber is an armstring ",0
    else:
        return "number is not an armstrong",1


# In[71]:


armstrong(1634)


# In[80]:


#Q.5 Write a Python Program to Find Armstrong Number in an Interval?
def armstrongbet(a,b):
    for num in range(a, b + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)
            
            
            
      


# In[83]:


armstrongbet(100,20000)


# In[84]:


# Q.6 Write a Python Program to Find the Sum of Natural Numbers?
def sumn(n):
    l=[]
    for i in range(0,n+1):
        l.append(i)
    a=0
    for j in l:
        a=a+j
    return a
    


# In[89]:


sumn(12345)


# In[ ]:




