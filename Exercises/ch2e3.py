# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 01:40:35 2017

@author: zil20
"""

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours > 40: 
        pay = 40 * rate + (hours-40) * rate * 1.5
    else: 
        pay = hours * rate
    print("Pay:", pay)
except:
    print("Error, please enter numeric input")
    