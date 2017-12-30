# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:39:17 2017

@author: zil20
"""
total = 0
count = 0
while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        num = float(num)
        count += 1
        total += float(num)
    except:
        print('Invalid input')
print(int(total), int(count), total/count)