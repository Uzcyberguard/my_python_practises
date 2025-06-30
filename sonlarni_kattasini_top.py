# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 18:57:41 2025

@author: User
"""

print("sonlarini eng kattasini topuvchi funksiya, >>> 7,6,78,10 tartibda sonlarni kiriting!") 
def eng_kattani_top():
    v=list(map(int,input('3 ta son kirit:').split(',')))
    maxi=max(v)
    return maxi
eng_katta=eng_kattani_top()
print(f"{eng_katta} bu ularning eng kattasi!")