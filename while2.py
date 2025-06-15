# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 15:33:05 2025

@author: User
"""

#1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, 
#yangi ro'yxatga joylang.
#2 e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
#3 Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
##                                      mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

#1-masala
buyurtmalar=[]
ism=input("ismingiz kim foydalanuvchi?>>>")
savol=f"{ism.title()} buyurtmalaringgizni birin ketin yozing?>>>"
while True:
    buyurtmalar.append(input(savol))
    a=input("yana yangi mahsulot buyurtma berishni hohlaysizmi? yes/no\n>>>")
    if a!="yes":
        break
print(f"bu sizning buyurtmalaringgiz {ism.title()}!👇")  
for buyurtma in buyurtmalar:
    print(buyurtma, sep=" ")

