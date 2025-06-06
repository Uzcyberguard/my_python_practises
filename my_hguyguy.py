# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 18:46:47 2025

@author: User
"""
n=int(input("katetni kirit:"))
son = 1
for i in range(1, n + 1):
        for j in range(i):
            print(son, end=' ')
            son += 1
        print()