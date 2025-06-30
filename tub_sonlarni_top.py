# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 19:32:53 2025

@author: User
"""

#foydalanuvchi sizga oraliq beradi, (5,9). shu oraliqdagi tub sonlar sonini topishim kerak.
def tub_sonlarni_top(a,b):
    ruyxat=list(range(a,b+1))
    for n in range(2,b+1):
        for son in ruyxat:
            if son%n==0 and son>n:
                ruyxat.remove(son)
    return ruyxat
a,b=map(int,input("oraliqni kirit: (exm: 5,56) >>> ").split(','))
tublar=tub_sonlarni_top(a,b) 
print(tublar) 