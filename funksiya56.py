# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 10:10:32 2025

@author: User
"""

# AMALIYOT
"""1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling
 (masalan, tel.raqam, el.manzil)
2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
 Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
4. Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida
 qaytaruvchi funksiya yozing
5. Berilgan oraliqdagi [tub sonlar](https://uz.wikipedia.org/wiki/Tub_sonlar_ro%CA%BByxati) ro'yxatini qaytaruvchi funksiya yozing 
(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
6. Foydalanuvchidan son qabul qilib, shu son miqdoricha [Fibonachchi ketma-ketligidagi]
(https://medium.com/@qudratxoja.musayev/fibonachchi-sonlari-va-u-haqida-qiziqarli-faktlar-47000a80264d) sonlar ro'yxatni qaytaruvchi
 funksiya yozing.  **Ta’rif**: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik
 Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  `1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...`"""
def info_private(ism, familiya, tyil, tjoy,yosh, email_manzil=None, tel_number=''):
   
    info={"ismi":ism,
          "familiyasi":familiya,
          "tugulgan_yili":tyil,
          "tugulgan_joyi":tjoy,
          "yoshi":yosh,
          "email_manzili":email_manzil,
          "telifon_raqami":tel_number
         }
    return info
odamlar=[]
while True:
      ism=input("isming nima:")
      familiya=input("familiya:")
      tyil=int(input("to'g'ulgan yiling: "))
      tjoy=input("tug'ulgan joying: ")
      yosh=input("yoshingni kirit: ")
      email_manzil=input("email manzil(majburiy emas): ")
   
      tel_number=input("telifon raqam(majburiy emas): ")

      odamlar.append(info_private(ism, familiya, tyil, tjoy,yosh, email_manzil=None, tel_number='')) 
      yana=input("yana odam qushsizmi? (ha/yoq): ")
      if yana !="ha":
         break
for odam in odamlar:
    print(f"{odam["ismi"].title()} {odam['familiyasi'].title()} {odam["tugulgan_yili"]}-yilda \
 {odam["tugulgan_joyi"].title()} da tug'ulgan.\n ")
    
    
    
    
    
    
    
    
    
    
    