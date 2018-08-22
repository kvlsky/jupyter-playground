
# coding: utf-8

# In[95]:


import numpy as np
import pandas as pd

data = pd.read_csv("data.csv", sep=',',encoding='utf-8')

for i in range(0,len(data.index)-2):
    str0 = data.loc[(i),'Heart rate']
    str1 = data.loc[(i+1),'Heart rate']
    str3 = data.loc[(i+2),'Heart rate']
    p = 0.1
    try:
        if str3 > str1 and str1 > str0 and str3 > str0:
            print("up")
        elif str0 > str1  and str1 > str3 and str0 > str3:
            print("down")
        elif abs(str3 - str1) <= str1 * p and abs(str0 - str1) <= str1 * p:
            print("stable")
        elif str1 > str0 and str1 > str3 and str1 - str0 >= str1 * p and str1 - str3  >= str1 * p:
            print("max")
        elif str0 > str1 and str3 > str1 and str0-str1 >= str1 * p and str3 - str1 >=  str1 * p:
            print("min")
    except:
        print("End of the table")


