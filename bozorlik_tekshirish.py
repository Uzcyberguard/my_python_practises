# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 21:23:16 2025

@author: Hasan
"""

mahsulotlar=["olma","kartoshka","sabzi","piyoz","sovun","soda","tarvuz","qovun","uzum","pamidor","bodring"]
bozorlik=[]
yuqlar=[]
borlar=[]
for mol in range(5):
     bozorlik.append(input(f"{mol+1} chi bozorlikni ayting>>>").lower())
for tovor in bozorlik :
  if tovor in mahsulotlar:
    borlar.append(tovor)
  else:
      yuqlar.append(tovor)
if len(borlar)==5: print("hamma mahsulot bor ekan😊") 
elif len(borlar)==0: print("bitta ham mahsulot yuq ekan😕") 
else:    
  print(yuqlar,'lar dukonda yuq')
  print(borlar,"lar dukonda bor")