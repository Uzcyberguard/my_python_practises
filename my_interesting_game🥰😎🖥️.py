# -*- coding: utf-8 -*-
#Created on Sun Jun 15 22:11:18 2025
# Hasan Normamatov ning birinchi sifatli o'yini, o'yin yoqqan bo'lsa xursandmiz🥰
print("\n \n WELCOME TO HASAN'S GAME\n")
qoida=input(("o'yin qonunlari haqida bilishni hohlaysizmi? (ha/yuq, qoidalarni bilaman)\n>>>").lower())
if qoida=="ha":
  print(" 'ZED' nomli o'yinimizga xo'sh kelibsiz! \
     \n bunda siz kompyuter sir saqlagan sonning BO'LUVCHISIni topishinggiz kerak.\
         \n QOIDALAR \
          \n Dastavval kompyuter biror sonni sir saqlaydi. Siz o'ylab ko'rib son aytasiz (bir sonni ikki marta aytish mumkin emas VA bo'luvchiga 1 ni kiritish ham'), agar soningiz kompyuter sir saqlagan sonning bo'luvchisi bo'lsa, sizga kompyuter u sonni aytadi va siz yutasiz.\
              \n Agar bo'luvchisi bo'lmasa, kompyuter o'zini sonidan sizning soninggizni ayiradi va hosil bo'lgan sonni yana sir saqlaydi.\
                  \n uyin shu tariqa davom etadi, \
                      \n \n ESLATMA!!! \n agar kompyuter sizning bir necha muaffaqiyotsiz yurishlaringgizdan keyin siz aytgan sonlarni o'zinikidan ayirib manfiy hosil qila olsa SIZ YUTQAZASIZ!!! \n Sir saqlangan son manfiy bo'lmasdan oldin uning bo'uvchisini toping!!")
tuplam=list(range(82,120,2))
for eliment in range(81,200,2):
   tuplam.append(eliment)
import random
sirr=random.choice(tuplam)
sir=sirr

print("\n  O'YIN BOSHLANDI😊 \n  OMAD!!!")  
sonlar=[1,6829797]    
print("kompyuterr sonni(80dan katta bo'lgan) sir saqladi!\n") 
buluvchi=input("BU SONNI BO'LUVCHISINI TOPISHGA URINIB KO'RING \n>>> ")
sir=sir-int(buluvchi)
if int(buluvchi) ==1 :
   bul=6829797
else:
   bul=int(buluvchi) 
sonlar.append(bul)
while int(sir)%int(bul) !=0 :
    bul=int(input("\n FAILED!!! \n Yangi sonni bo'luvchisini topishga YANA urinib ko'ring!!😉😊>>>"))
    if bul in sonlar:
        print("\n SIZ IKKI MARTA BIR XIL SON KIRITDINGGIZ yoke BO'LUVCHIGA 1 NI KIRITDINGGIZ😕 \n \n bu son inobatga olinmadi!!!")
        bul=sir+1
        continue
    else:    
        sonlar.append(bul)
    
    
    sir=sir-bul
    if sir<0:
        print(f"Afsus Komputer yutdi🖥️.\n Kompyuter sir tutgan son dastlab {sirr} edi, keyin o'zgarishlardan keyin {sir} bo'ldi va bu manfiy son!😒😕😖")
        break
if sir>0:    
    print(f" YOU WON!!!💐🏆🏆🏆😉 \n Kompyuter sir tutgan son dastlab {sirr} edi, keyin o'zgarishlardan keyin {sir+bul} bo'ldi va siz uni bo'luvchisini {bul} ni topdinggiz!😎")    
print("o'yinimiz yoqqan bo'lsa xursandman🤗")    





























































































































