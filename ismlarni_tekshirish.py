# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 22:48:41 2025

@author: Hasan
"""
a=[]
foydalanuvchilar=["hasan","husan","dilshod","asilbek","asad"]
new_user=input("foydalanuvchi loginini tanlang!!!>>>").lower()
for ism in foydalanuvchilar:
    if new_user==ism:
        print(f"xush kelibsiz!!! {new_user.title()}")
    if new_user !=ism:
        a.append(ism) 
if len(a)==5:        
      print(f" {new_user.title()} Uzr!\n siz band login tanladinggiz!\n Boshqa login tanlang")
