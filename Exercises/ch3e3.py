# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:37:07 2017

@author: zil20
"""

try: 
    score = float(input("Enter score: "))
    if 0.0 <= score < 0.6:
        print("F")
    elif score < 0.7:
        print("D")
    elif score < 0.8:
        print("C")
    elif score < 0.9:
        print("B")
    elif score <= 1.0: 
        print("A")
    else:
        print("Bad score")
except:
    print("Bad score")  