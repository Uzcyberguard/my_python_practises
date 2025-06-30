# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 09:33:24 2025

@author: User
"""
baholar={}
def bahola(students):
    for student in students:
        baho=input(f"{student.title()}ning bahosini quying!>> ")
        
        baholar[student]=baho
    return baholar
ruyhat=['asil','husan','hasan','olim','abbos']   
tabil=bahola(ruyhat) 
for ism , baho in tabil.items():
    print(f"{ism}ning bahosi {baho}")