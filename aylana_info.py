# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 19:19:48 2025

@author: User
"""

def aylana_par(r):
    info={}
    info['diametr']=2*r
    info["radius"]=r
    info["uzunligi"]=2*3.14*r
    info["yuzi"]=3.14*(r**2)  
    return info
r=float(input("aylana radiusini kiriting!>> "))
print(aylana_par(r))