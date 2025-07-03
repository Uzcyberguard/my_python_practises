# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:58:42 2025

@author: User
"""

def mmmhasan():
    import random 
    print("endi siz son o'ylang men topaman")
    ask=input("son o'ylab bo'lsangiz 'ok' deb yozing>> ")
    toplam=[1,2,3,4,5,6,7,8,9,10]
    tahminlar=1
    while True:
        guess=random.choice(toplam)
        print(f"\nSiz o'ylagan son {guess} edimi?\n")
        javob=input(f"agar javobingiz {guess} bo'lsa (T),{guess}dan kichik bo'lsa (-), katta bo'lsa (+) yoz>> ")
        if javob.lower()=="t":
            break
        elif javob=="-":
        
            toplam = [num for num in toplam if num < guess]
            tahminlar+=1        
            continue
                    
        elif javob=="+":
             
             toplam = [num for num in toplam if num > guess]
             tahminlar+=1        
             continue        
    
    return tahminlar  
    