# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 16:55:38 2025

@author: User
"""

menyu={"osh":23000,"manti":34000,"somsa":7000,"sho'rva":30000,"lavash":40000,"hotdog":10000,"dena":15000,"non":4000,"lag'mon":27000}
a=[]
for n in range(3):
  a.append(input(f"{n+1} chisiga nima buyurtma qilasiz?>>>").lower())
for tanlov in a:
    if tanlov in menyu:
        print(f"{tanlov}ning narxi {menyu[tanlov]}")
    elif tanlov not in menyu and tanlov !="cola" :
        print(f"bizda {tanlov} yuq ekan")
    elif tanlov=="cola":
        b=float(input("bizda turli o'lchamli cola mavjud.\n Necha litrlik cola olmoqchisiz?>>>"))
        if b==1:
                     print(f"{b} litrli cola bizda 14000")
        if b==1.5:
                     print(f"{b} litrli cola bizda 17000")          
  