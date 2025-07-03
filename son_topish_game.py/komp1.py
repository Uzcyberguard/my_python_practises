# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:44:13 2025

@author: User
"""
def komp():
    import random as r 
    son=r.randint(1,10)
    urinishlar=1
    tahmin=int(input("1dan 10 gacha son o'yladim topishga urinib ko'ring\n>> "))
    while True:
        if son==tahmin:
            print("siz topdinggiz")
           
            break
        elif son>tahmin:
            print(f"men uylagan son {tahmin} dan katta")
            tahmin=int(input("yana urinib ko'ring>> "))
            urinishlar+=1
            continue
        elif son<tahmin:
            print(f"men uylagan son {tahmin} dan kichik")
            tahmin=int(input("yana urinib ko'ring>> "))
            urinishlar+=1
            continue
    print(f"siz {urinishlar} marta urinib men o'ylagan so'zni topdingiz?")  
    return urinishlar