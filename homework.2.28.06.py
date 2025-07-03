# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 18:10:37 2025

@author: User
"""

#  Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
#Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy
# ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_malumot_ber(ism,familya,**qoshimcha):
    info={}
    info["talaba ismi"]=ism
    info["talaba familyasi"]=familya
   
    for kalit,mal in qoshimcha.items():
        print (f"{kalit} => {mal}")
    return info    
ism=input("isming kim?>> ")   
familya=input("familyang nima? >> ") 
talaba=talaba_malumot_ber(ism,familya,sinfi="11",tel="23473978692")   
print(talaba) 
 