# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 11:46:28 2025

@author: User
"""


"""1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling
 (masalan, tel.raqam, el.manzil)
2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
 Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
4. Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida
 qaytaruvchi funksiya yozing.
5. Berilgan oraliqdagi [tub sonlar](https://uz.wikipedia.org/wiki/Tub_sonlar_ro%CA%BByxati) ro'yxatini qaytaruvchi funksiya yozing 
(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
6. Foydalanuvchidan son qabul qilib, shu son miqdoricha [Fibonachchi ketma-ketligidagi]
(https://medium.com/@qudratxoja.musayev/fibonachchi-sonlari-va-u-haqida-qiziqarli-faktlar-47000a80264d) sonlar ro'yxatni qaytaruvchi
 funksiya yozing.  **Ta’rif**: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik
 Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  `1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...`"""
 
def febanachilar_ruyhati(n):
    fib=[1,1]
    if n==1:
        print(fib[0])
    elif n==2:
        print(fib[0],fib[1])
    else:
        
        m=n-2
        while m>0:
            keyingi=fib[-1]+fib[-2]
            fib.append(keyingi)
            m-1
    return fib
n=int(input("nechta febanachi qatorni tashkil etmoqchisiz: "))
fibanachilar=febanachilar_ruyhati(n)
for a in fibanachilar:
    print(n, end=",")        
            
        
        
          
    


    