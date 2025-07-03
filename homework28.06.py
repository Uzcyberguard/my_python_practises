# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 18:05:59 2025

@author: User
"""

#1  Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi 
# harfini katta harfga o'zgatiruvchi funksiya yozing.
#2  Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat
# qaytaradigan qilib o'zgartiring
#3  Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va 
# asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

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