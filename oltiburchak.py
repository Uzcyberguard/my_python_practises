# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 11:15:05 2025

@author: User
"""

a=int(input())
c=1
if a==1:
  print(1)#
else:
#son=6*(n-1)-2n+3=4n-3
    for n in range(2,a+1):
        c+=4*n-3
    print(int(c))