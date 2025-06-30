# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 10:00:23 2025

@author: User
"""

def sonlar_kopaytir(*sonlar):
  
    a=1
    for son in sonlar:
        a=a*son
    return a
sonlar=list(map(float,input("write numbers as much as you want, we will tell you their product>> ").split(" ")))
products=sonlar_kopaytir(*sonlar)
print(products)     