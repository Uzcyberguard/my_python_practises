# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:47:20 2025

@author: User
"""
son=[]
a=int(input())
b=list(map(int,input().split()))
# b=n*(n+1)/2> 2b=n**2+n
       # -1+ild(1+8b)      
for n in list(b):
    s=(1+8*n)**(1/2)
    if n>int(a*(a+1)/2):
           son.append(0)
    elif s.is_integer():
       	   son.append(1)
    else:
           son.append(0)


sonn = int(''.join(str(x) for x in son))
print(sonn)  
       