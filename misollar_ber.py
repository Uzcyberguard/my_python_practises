# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:58:54 2025

@author: User
"""
correct=0
incorrect=0
n=1
print("\n xush kelibsiz mening matematikaga asoslangan o'yinimga!.\n")
while True:
    import random
    a=random.randint(2,100)
    b=random.randint(30,200)
    c=random.randint(20,300)
    d=random.randint(1,20)
    e=random.randint(3,35)
    print(f"{n}-misolni yech👇")
    savol=f"{c*d}:{d}="
    misol1=f"{b+c}-{a}="
    misol2=f"{a}+{b}="
    misol3=f"{e}*{d}="
    muu=[misol1,misol2,misol3,savol]
    misol=random.choice(muu)
    if misol==misol1:
        javob=b+c-a
    elif misol==misol2:
        javob=a+b
    elif misol==misol3:
        javob=e*d
    else:
        javob=c
    yechim=input(misol)
    if int(yechim)==int(javob):
        print("   To'g'ri!")
        correct+=1
    else:
        print("   Noto'g'ri!")
        incorrect+=1
    davom_et=input("  davom etish uchun 'enter' ni bos!\n  to'xtatish uchun 'stop' deb yoz. \n>>>")  
    if davom_et=="":
        n+=1
        continue
    elif davom_et=="stop":
        break
print("xursandmiz agar o'yinimiz sizga yoqqan bo'lsa!")
print(f"siz {correct} ta misolni to'g'ri yechdingiz, {incorrect} ta misolni esa xato yechdingiz.")
        