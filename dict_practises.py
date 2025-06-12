# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 22:26:22 2025

@author: User
"""

poytaxt={"uzbekiston":"toshkent","rassiya":"maskva","america":"new york"}
poytaxt["hindiston"]="dehli"
poytaxt["ukraina"]="kiev"
poytaxt["mexiko"]="mexika"
for h,v in poytaxt.items():
    print(h.upper())
    print(v.title())    
    print()