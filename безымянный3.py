# -*- coding: utf-8 -*-
"""
Created on Thu May 29 17:00:48 2025

@author: User
"""
a,b,c=map(int,input("kvadrat tenglamani koiffesentlarini kirit:").split())
d=b**2-4*a*c
x1=(-b+d**(1/2))/(2*a)
x2=(-b-d**(1/2))/(2*a)
if d<0:
    print("tenglamani haqiqiy yechimi yuq")
else:         

   print("x1=", x1,"  x2=",x2)