# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 16:40:43 2025

@author: User
"""

poytaxt={"uzbekiston":"toshkent","rassiya":"maskva","america":"new york"}
poytaxt["hindiston"]="dehli"
poytaxt["ukraina"]="kiev"
poytaxt["mexiko"]="mexika"
poytaxt["germaniya"]="berlin"
a=str(input("qaysi davlat poytaxti haqida bilmoqchisan?>>>").lstrip().lower())
if a in poytaxt:
        print(f"{a.title()}ning poytaxti {poytaxt[a].title()}" )
else:
        print("bizda u haqida malumot yuq")