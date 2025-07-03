# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:19:01 2025

@author: User
"""
print("son topish o'yinimizga xush kelibsiz!")
while True:
    urinishlar=0
    print("men 1 dan 10 gacha son o'yladim, topishga urinib ko'ringchi!?")
    import random as r
    son=r.randint(1,10)
    tahmin=int(input(">> "))
    if tahmin==son:
        break
    elif tahmin>son:
        print(f"o'ylangan son {tahmin} dan kichik")
        urinishlar+=1
        