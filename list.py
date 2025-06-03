# -*- coding: utf-8 -*-
"""
Created on Thu May 29 08:56:18 2025

@author: User
"""

frinds=[]
#mening to'g'ulgan kunimga keladigan mehmonlar ruyxati
frinds.append("oybek".upper())
frinds.append("asil".capitalize())
frinds.append("Asad")
frinds.append("dilshod".capitalize())
mehmonlar=[frinds[0],frinds[1],frinds[2],frinds[3]]
# Oybekni ishi chiqib qoldi. Asad kelolmas ekan.
#2 kundan keyin ulardan 2tasi kelolmas ekan.
kelganlar=[mehmonlar.pop(0),mehmonlar.pop(1)]
# samarqanddan ham mehmonlar kelib qolishdi.
kelganlar.append("muhob opa".upper())
# qo'shnimiz Mavluda opa ham ayamni to'g'ulgan kuniga kelishdi.
kelganlar.insert(0,"mavluda opa".title())
del kelganlar[3]
kelganlar.insert(465,"Qudrat pochcha")
#kelganlar.append("To'lg'on amma")
print(sort(kelganlar))
