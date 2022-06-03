#!/usr/bin/env python
# coding: utf-8

# Q.1 What are the two values of the Boolean data type? How do you write them?  
# Ans: there are two Boolean data type  
#     1. True  
#     2. False

# Q.2 What are the three different types of Boolean operators?   
# Ans: AND, OR,NOT
# 

# Q.3 Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).  
# Ans:  
#     NOT  
#     0 -1   
#     1 -0       
#     AND      
#     0 0  - 0  
#     0 1  - 0   
#     1 1  - 1  
#     1 0  - 0  
#     OR      
#     0 0  - 0  
#     0 1  - 1  
#     1 1  - 1  
#     1 0  - 1   
#     
#     
#     

# Q.4 What are the values of the following expressions?      
# (5 &gt; 4) and (3 == 5)     
# not (5 &gt; 4)      
# (5 &gt; 4) or (3 == 5)     
# not ((5 &gt; 4) or (3 == 5))   
# (True and True) and (True == False)  
# (not False) or (not True)  
# 

# In[9]:


#ANS
print((5>4) and (3==5))# Flase
print( not(5>4)) # False
print((5>4) or (3==5))# True
print(not((5>4) or 3==5))# False
print((True and True) and (True==False))
print(not False) or (not True)


# Q.5 What are the six comparison operators?  
# Ans:   
#  > -Greater   
# < - lesser  
# <= -less equal  
# >= -grewater equal to  
# !=  -not equal to   
# == - equal 

# Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.  
# Ans: equal to means we are providing a value to some variable but in other in assigmnet operator we are operating someting (operating will be done)
# 

# In[12]:


#Ex:
a=5
b=6 # assign a value of a variavle name b
#a=a+b
a+=b  # Assignment operation
print(a)


# Q.7 Identify the three blocks in this code:  
# spam = 0   
# if spam == 10:  # block1   
# print(&#39;eggs&#39;)     
# if spam &gt; 5:      #block2  
# print(&#39;bacon&#39;)    
# else:     #block 3   
# print(&#39;ham&#39;)    
# print(&#39;spam&#39;)    
# print(&#39;spam&#39;)    
# ANs:  here there are three blocks if 

# In[17]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# Q.8 Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.   
# 
# 

# In[20]:


spam=int(input("enter your number"))
if spam==1:
    print("spam")
elif spam == 2:
    print("Howdy")
else:
    print('Greetings')


# Q.9 9.If your programme is stuck in an endless loop, what keys you’ll press?  
# Ans: CTRL+C

# Q.10 How can you tell the difference between break and continue?  
# ANs: very major difference between break and continue is that when we apply break operation it will stop the programme and come out  
#     but at the same time when we apply continue opeation it will not print only that condition which is False and then contibue the programme and run for further condition

# In[25]:


#Ex break :;
for i in range(10):
    if i==5:
        break
    print(i)
print(" this is end of  the brea")
    
for j in range(0,10):
    if j ==5:
        continue
    print(j)
    


# In[34]:


##Q 11 In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?  
for i in range(10):
    print(i)
print(" range(10) end    ")

for i in range(0,10):
    print(i)
print('range(0,10) end')
for i in range (0,10,1):
    print(i)
print("range(0,10,1) end")


#  Q.12 Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.
# 

# In[33]:


for i in range(1,11):
    print(i)
print("code in while loop")
i=0
while i<10:
    i+=1
    print(i)


# Q .13 If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam   
# Ans: from bacon() import spam  
# spam.bacon()
# 

# In[ ]:




