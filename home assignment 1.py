#!/usr/bin/env python
# coding: utf-8

# ## questions 
# a="this is my first python programming class and a am learning python string and it's function"
# 1. try to extract data from index one to 100 with a jump of 3
# 2. try to reverse the string without using reversr function
# 3. try to split a string after conversion of entire string uppercase
# 4. try to convert the whole string into lower case
# 5. try to capatlize the whole string
# 6. write a difference between isalnum() and isalpgha()
# 7. try to give an example of sxpand tab
# 8. give an example of strip,istrip, and r strip
# 9. replace a string character by another charactor by taking your own example
# 10. try give a defnition of sring centre function with example
# 11. write your own defnition of compiler and inrerpretor
# 12. python is a interpreted or compiled language give a clear answer
# 13. try to write usecase of python with your understading

# In[1]:


a= "this is my first python programming class and a am learning python string and it's function"


# In[5]:


a[1:101:3] #extract data from index one to 100 with a jump of 3


# In[6]:


a[::-1]# reverse the string 


# In[13]:


b=a.upper()


# In[14]:


b


# In[15]:


b.split(" ")#split a string after conversion of entire string uppercase


# In[16]:


b.lower()# convert the whole string into lower case


# In[21]:


c=a.split(' ')


# In[22]:


c


# In[25]:


a.capitalize() # capatlize the whole string


# ## write a difference between isalnum() and isalpgha()
# 1. isalnum(): 
# it is a function return true for a sting if a string have alphabetical and nummercal character both present in string and at least 
# one character should be there in the string.
# 2. isalpha():
# it is a function return true if a string have only alphabetical value otherwise it will give false and atleast one character should be there 
# 
# 

# In[28]:


## try to give an example of expand tab
str = "ilovepython"


# In[29]:


str.expandtabs(2)


# In[34]:


#give an example of strip,istrip, and r strip
b='    upendra      '


# In[35]:


b.strip()#it drope the character of leading and trailind character but by default it take blank space


# In[40]:


txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")


# In[41]:


x


# In[48]:


t='this is upendra code'
t.strip("te")


# In[54]:


t.rstrip('eod') #delete tailing chars


# In[56]:


t.lstrip('th')#delete leading chars


# In[62]:


t.replace('e','r') #replace e with r


# ## defnition of sring centre function with example string centre is defined in this way,
# it is a function that centalize the whole string , it takes two input character width which means how many chars in output will be and 2nd what chars you want to add this chars will be added as leading and tailing chars
# ## example

# In[72]:


s='upendra'
s.center(34,'$')


# In[ ]:


## write your own defnition of compiler and inrerpretor
1. complier 
-  


# In[ ]:





#  ## write usecase of python with your understading
#     use of python language is very vast 
#     1. in Business analysis
#     1. web development
#     3. AI
#     4. Game development
#     5. mobile apps 
#     many more 
#     
