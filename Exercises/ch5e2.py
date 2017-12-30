# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:49:36 2017

@author: zil20
"""
smallest = None 
largest = None
while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = float(num)
        if smallest == None or num < smallest:
            smallest = num
        elif largest == None or num > largest:
            largest = num
    except:
        print('Invalid input')
print(largest, smallest)