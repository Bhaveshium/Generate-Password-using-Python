#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random


# In[8]:


#entering length of the password
passlen = int(input("Enter the length of password : "))

#The set of variables to create password
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"

#creating a random string for password
p = "".join(random.sample(s,passlen ))
print(p)

