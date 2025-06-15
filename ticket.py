# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 14:19:50 2025

@author: User
"""

#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
#18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin 
#va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
#Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

yoshi=''
while yoshi !="quit" or yoshi != "stop":
    yoshi=(input("yoshingizni kiriting ( dasturni to'xtatish uchun 'stop' yoke 'quit' deb yozing!)>>>"))
    if yoshi=="stop" or yoshi=="quit":
        break
    yosh=int(yoshi)
    if yosh<7:
        print("chipta 2000 so'm sizga\n")
    elif yosh<18 and yosh>=7:
        print("sizga chipta 3000 so'm\n" )
    elif yosh>=18 and yosh<65:
        print("sizga chipta 10000 so'm\n")
    else:
        print("bepul sizga\n")
print("\nyordamimiz tegkan bo'lsa rahmat🤗🥰")    