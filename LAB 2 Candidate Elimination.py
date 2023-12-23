#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


d = pd.read_csv(r'C:\Users\kumar\Desktop\DataSet\2-5\2\lab2.csv')


# In[14]:


print(d)


# In[15]:


d


# In[16]:


array = np.array(d)[:,0:-1]


# In[17]:


array


# In[18]:


target = np.array(d)[:,-1]


# In[19]:


target


# In[9]:


print("n Attributes are : ",a)
n_att = len(a[0])


# In[ ]:


print("No. of Attribute ",n_att)


# In[11]:


print("The initial Hypothesis is : ")
hypothesis = [0]*n_att
print(hypothesis)


# In[10]:


def train(a,t):
    for i, h in enumerate(a):
        print("\nInstance", i+1 , "is ", h)
        if t[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(a)):  # specific a
                if h[x]!= a[x]:      #  general t            
                    a[x] ='?'                     
                    a[x][x] ='?'
                   
        if t[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(a)): 
                if h[x]!= a[x]:                    
                    t[x][x] = a                
                else:                    
                    t[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", a)         
        print("Generic Boundary after ", i+1, "Instance is ", t)
        print("\n")

    indices = [i for i, val in enumerate(t) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        t.remove(['?', '?', '?', '?', '?', '?']) 
    return a, t 

s_final, g_final = train(a, t)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")


# In[ ]:




