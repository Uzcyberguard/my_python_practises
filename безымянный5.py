# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 16:17:07 2025

@author: User
"""

"""AMALIYOT
1)Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
2)Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3)Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4)Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
 Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
5)Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.
Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
6)Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
 Natijalarni konsolga chiqaring."""
sonlar=list(range(2,11))
def qoldiq(x):
    for son in sonlar:
        a=x%son
        print(f"{x} ni {son} ga bo'lgandagi qoldiq {a} ga teng")    
    
qoldiq(x=11) 

    