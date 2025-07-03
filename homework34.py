# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 11:33:39 2025

@author: User
"""


def matn_katta_harf(matnlar):
    
        return matnlar
malumotlar=[]    
while True:
   mal=input("malumot kiriting (agar hohlamasangiz 'yoq' deb yozing?): " )
   if mal !="yoq":
       malumotlar.append(mal)
   else:
       break
v=matn_katta_harf(malumotlar)   
for q in v:
    print(q.capitalize())