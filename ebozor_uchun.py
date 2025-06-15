# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 20:32:14 2025

@author: User
"""

#1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, 
#yangi ro'yxatga joylang.
#2 e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
#3 Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
##                                      mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
narxlar={}
savol1="mahsulot nomini kiriting!>>>"
n=1
while True:
      savol1=f"{n}-mahsulot nomini kiriting!>>> "
      mahsulot=input(savol1)
      n+=1
      savol2=f"{mahsulot} narxini kiriting!>>> "
      narx=input(savol2)
      narxlar[mahsulot]=narx
      c=input("yana mahsulot kiritishni hohlaysizmi?🤗😊🥰(yes/no)\n>>>")
      if c !="yes":
          break
print("biz bilan e-bozor mahsulot narxlari ruyxatini yaratganiz uchun katta rahmat!😉")
for tovar, pul in narxlar.items():
    print(f"{tovar} ning narxi {pul}")  
print("bu sizning ruyxatinggiz🥰")    