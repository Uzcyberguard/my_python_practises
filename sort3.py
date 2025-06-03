# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 10:43:34 2025

@author: Hasan
"""
odamlar=[]
soni=int(input("bugun nechta odam bilan ko'rishdingiz: "))
if soni==0:
    print("uyda yot unda.😣, bir ko'chaga ham chiqib tur😂")
else:    
  for n in range(int(soni)):
    odamlar.append(input(f"bugungi {n+1} chi bo'lib ko'rishgan odamingiz kim?:")) 
print(odamlar," lar bilan ko'rishibsiz bugun😉😉😉")         
