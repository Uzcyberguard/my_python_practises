# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 10:54:23 2025

@author: User
"""

a=list(map(int,input().split()))
b=int(input())
if sum(list(a))>=b:
   print(0)
else:
   print(b-sum(list(a)))