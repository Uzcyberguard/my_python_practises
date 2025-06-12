# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 08:40:22 2025

@author: User
"""

a=str(input("o'zbek tilida so'z kirit, men senga inglizchasini aytaman.>>>").lower())
lug={"olma":"apple","tarvuz":"watermelon","qovun":"melon","kitob":"book","maktab":"school"}
if a.lstrip() in lug:
    print(f"{a}ning tarjimasi ingliz tilida '{lug[a.lstrip()]}'")
else:
    print("bunday so'z bizni lug'atda yuq ekan, uzr" )          