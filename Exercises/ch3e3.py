# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:37:07 2017

@author: zil20
"""

def computegrade(score):
    if 0.0 <= score < 0.6:
        return "F"
    elif score < 0.7:
        return "D"
    elif score < 0.8:
        return "C"
    elif score < 0.9:
        return "B"
    elif score <= 1.0: 
        return "A"
    else:
        return "Bad score"
try: 
    score = float(input("Enter score: "))
    print(computegrade(score))
    
except:
    print("Bad score")  