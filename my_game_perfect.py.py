# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 22:50:25 2025

@author: User
"""


#rules
rules="This is interesting game based on number theory, in this game \
computer memorises a munber(100;200) as a secret and you need to find this \
number's factor for winning.\
If your number is not factor of this number, computer subtracts your number from secret.\
   \n   \n NOTE \n\n When SECRET REACHS TO NEGATIVE SCALE or YOU BREAK RULES THREE TIMES \
in terms of WRITING 1 and WRITING ONE NUMBER TWICE as a factor."
print("Welcome to Hasan's game") 
qoida=input("\n Do yuo want to know about the game's roles (yes\ no)\n>>> ") 
if qoida=="yes":
  print(rules)
                  
yana=True
while yana==True:
    print("\n LET'S GO TO START THE GAME!!!")
    import random
    sirr=random.choice(list(range(100,201)))
    sir=sirr
    #random tanlaydi
    tanlovlar=[1]
    n=0

    while True:
        if n==3 :
            print(f"YUO LOST \n becauce you broke the rules at three times! \n \n The secret intially was {(sirr)}")
            break
        if sir<0:
            print("computer is WINNER!!!")
            print(f"\n The secret intially was {(sirr)} and after some steps it had become {(sir)} ,but this is negative ")
            break
        tanlov=int(input("\n please, try to find a factor of this secret number!\n>>> "))
        if tanlov==1:
            n+=1
            print(f"\n You have broken {n} times the rules because writing 1 is forbiden!!!")
       
            continue
        elif tanlov in tanlovlar:
            n+=1
            print(f"\n you have broken {n} times the rules by writing same number as a factor at two times! ")
      
            continue
        else:
            tanlovlar.append(tanlov)
            if sir%tanlov==0:
                print("\n YOU WON!!!")
                print(f"\n The secret intially was {(sirr)} and after some steps it had become {(sir)} ,and then you have found its factor that is {(tanlov)} ")
                break
            else:
                sir=sir-tanlov
                print("\n you could not find factor of this secret number.")
                continue
    qayta_uynash=input("\n Would you play again? (yes/no)>>> ")
    if qayta_uynash=="yes":
                yana=True
    else:
                yana=False
print("\n If you are interested in my game , I am so glad.")        
# 2 ,3 4, 6, 16, 12.        
   
        
    
