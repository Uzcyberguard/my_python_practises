# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 22:50:25 2025

@author: User
"""

print("O'YINNI BOSHLAYMIZ")
import random
sir=random.choice(list(range(100,201)))
#random tanlaydi
tanlovlar=[1]
n=0

while True:
    tanlov=int(input("sonni kirit: "))
    if tanlov in tanlovlar:
        print("siz ikki marta bitta sonni kiritdinggiz va qoidani buyzdinggiz! ")
        n+=1
        continue
    else:
        tanlovlar.append(tanlov)
    if sir%tanlov==0:
        print("YOU WON!!!")
        break
    else:
        sir=sir-tanlov
    if n==3 or sir<0:
        print("YUO LOST")
        break
        
    