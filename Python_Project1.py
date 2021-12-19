#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input("enter the number="))
count=0
if(n>1):
    for i in range(2,n):
        if (n % i)==0:
            count=count+1
    if count>=1:
        print ("Entered number is composite number")
    else: 
        print ("Entered number is prime number")
        


# In[37]:


import math

a = int(input("enter the 1st side of traingle="))
b = int(input("enter the 2nd side of traingle="))
f=(a**2)+(b**2)
c= math.sqrt(f)
print ("The third side of the triangle is", c)


# In[49]:


a = "I love my India and I live in Mumbai"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print ("Result"+str(b))


# In[10]:


count=0
a = str(input("Enter the string"))
b=len(a)
c=b//2
for i in range(0,c):
    if a[i]==a[b-i-1]:
        count=count+1
if count==c:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


Fact=1
n = int(input("enter the number="))
if n < 0:
    print ("Factorial not defined for -ve number")
elif n==0:
    print ("Factorial is always 1 for Zero")
else: 
    for i in range(1,n + 1):
        Fact= Fact*i
    print("The factorial of",n,"is", Fact )

