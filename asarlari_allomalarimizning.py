# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 16:10:39 2025

@author: User
"""

alloma1={"ism":"alisher navoiy","tyili":1441,"tjoyi":"hirot","vafyili":1501}
alloma2={"ism":"amir temur","tyili":1336,"tjoyi":"xo'ja ilg'or qishlog'ida","vafyili":1405}
alloma3={"ism":"erkin vohidov","tyili":1936,"tjoyi":"farg'ona","vafyili":2016}
alloma4={"ism":"abdulla qodiriy","tyili":1894,"tjoyi":"toshkent","vafyili":1938}




allomalarimiz=[alloma1,alloma2,alloma3,alloma4]
allomalarimiz[0]["asarlari"]=["xamza","mahbub ul qulub","farhod va shirin"]
allomalarimiz[1]["asarlari"]=["temur tuzliklari","temuriylar tarixi"]
allomalarimiz[2]["asarlari"]=["nido dostoni","daftar hoshiyasidagi bitiklar"]
allomalarimiz[3]["asarlari"]=["o'tgan kunlar","mehrobdan chayon"]   

for alloma in allomalarimiz:
    print(f" {alloma['ism'].title()}ning yozgan asarlari:")
    for asar in alloma["asarlari"]:
        print(asar.title(), end=", ")
    print()