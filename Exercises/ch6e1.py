# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:05:19 2017

@author: zil20
"""

fruit = 'banana' 
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1
print(fruit[:])
