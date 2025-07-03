# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:33:09 2025

@author: User
"""
import komp1 
import mmm123
while True:
    print("O'yinni boshlaymiz!")
  
    q2=komp1.komp()
    q1=mmm123.mmmhasan()
    if q2>q1:
        print(f" Men yutdim🖥️🏆!!!\n siz {q2} marta urinishda sonni topdingiz, men esa {q1} marta urinishda topdim")
    elif q2<q1:
        print(f" Siz yutdingiz😎🏆!!!\n siz {q2} marta urinishda sonni topdingiz, men esa {q1} marta urinishda topdim")
    else:
        print(f" Do'stlik g'alaba qildi🤝!!!\n siz {q2} marta urinishda sonni topdingiz, men ham {q1} marta urinishda topdim")
    yana=input("\nyana davom ettirasizmi?(yes\ no)>> ")
    if yana.lower()=="yes":
        continue
    else:
        break