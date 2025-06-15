# -*- coding: utf-8 -*-
#Created on Sun Jun 15 22:11:18 2025
# Hasan Normamatov ning birinchi sifatli o'yini, o'yin yoqqan bo'lsa xursandmiz🥰
import random
sirr=random.choice(list(range(80,200)))
sir=sirr
print("ZED nomli o'yinimizga xo'sh kelibsiz! \
     \n bunda siz kompyuter sir saqlagan sonning bo'luvchisini topishinggiz kerak.\
         \n QOIDALAR \
          \n siz o'ylab ko'rib son aytasiz, agar soningiz kompyuter sir saqlagan sonning bo'luvchisi bo'lsa, sizga kompyuter u sonni aytadi va siz yutasiz.\
              \n Agar bo'luvchisi bo'lmasa, kompyuter o'zini sonidan sizning soninggizni ayiradi va hosil bo'lgan sonni yana sir saqlaydi.\
                  \n uyin shu tariqa davom etadi, \
                      \n \n ESLATMA!!! \n agar kompyuter sizning bir necha muaffaqiyotsiz yurishlaringgizdan keyin siz aytgan sonlarni o'zinikidan ayirib manfiy qila olsa SIZ YUTQAZASIZ!!!")
a=input("o'yinni boshlaymizmi? \n (yes\ no)>>> ")  
if a !="yes":
   print("o'ziz bilasiz, baribir o'yin boshlanadi.🤪\n")  
    
print("kompyuterr sonni(80dan katta bo'lgan) sir saqladi\n") 
buluvchi=input("siz bo'luvchisini ayting endi? \n Yaxshilab o'ylab ayting>>> ") 
bul=int(buluvchi)
while int(sir)%int(bul) !=0 :
    sir=sir-bul
    bul=int(input("eh , soninggiz sir saqlangan sonni bo'luvchisi emas ekan. Sir saqlangan son endi o'zgardi.\
                  \n E'tiborliroq va zukkoroq bo'lib yangi sonni bo'luvchisini topishga urinib ko'ring!!😉😊>>>"))
    if sir<0:
        print("afsus Komputer yutdi🖥️😎")
        break
if sir>0:    
    print(f"qoyil siz yutdinggiz💐🏆🏆🏆😉 \n Kompyuter sir tutgan son dastlab {sirr} edi, keyin o'zgarishlardan keyin {sir} bo'ldi va siz uni bo'luvchisini {bul} ni topdinggiz!😎")    
print("o'yinimiz yoqqan bo'lsa xursandman🤗")    





























































































































