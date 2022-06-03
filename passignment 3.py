#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1  Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=int(input("enter the number: "))
if a>0:
    print("enter number is positive")
elif a<0:
    print("enter number id negative")
else:
    print("enter nmuber is zero")


# In[2]:


# Q.2.  Write a Python Program to Check if a Number is Odd or Even?
n=int(input("enter your number :"))
if ( n%2==0):
    print("number is even")
else:
    print("number is odd")
 


# In[3]:


#Q.3 Write a Python Program to Check Leap Year?
n=int(input("enter the year: "))
if (n%400==0) and (n%100==0):
    print("enter year is leap year".format(n))
elif (n%4==0) and (n%100!=0):
    print("enter year is leap year".format(n))
else:
    print("enter year is not leap year".format(n))


# In[4]:


# Q.4 Write a Python Program to Check Prime Number?
n=int(input("enter you number:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
if len(l)==2:
    print("enter number is prime")
else:
    print('enter number is not prime')
    
            


# In[29]:



def isprime(n):
    
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    
    if len(l)==2:
        return 0
    else:
        return 1

            
        
    


# In[30]:


isprime(15)


# In[28]:


for i in range(1,10001):
    l=0
    for j in range(2,(i//2+1)):
        if (i%j==0):
            l=l+1
            break 
    if (l==0 and i!=1):
        print("%d" %i,end=" ")


# In[ ]:




