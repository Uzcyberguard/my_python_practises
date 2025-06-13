# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 15:44:40 2025

@author: User
"""

alloma1={"ism":"alisher navoiy","tyili":1441,"tjoyi":"hirot","vafyili":1501}
alloma2={"ism":"amir temur","tyili":1336,"tjoyi":"xo'ja ilg'or qishlog'ida","vafyili":1405}
alloma3={"ism":"erkin vohidov","tyili":1936,"tjoyi":"farg'ona","vafyili":2016}
alloma4={"ism":"abdulla qodiriy","tyili":1894,"tjoyi":"toshkent","vafyili":1938}
allomalarimiz=[alloma1,alloma2,alloma3,alloma4]
for alloma in allomalarimiz:
     print(f"Allomamiz {alloma['ism'].title()} {alloma['tyili']}-yilda {alloma['tjoyi'].title()}da tug'ulgan."
           f"Afsuski  {alloma['ism'].title()} {alloma['vafyili']}-yilda olamdan o'tgan.\n ")