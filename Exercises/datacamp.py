# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 01:13:35 2018

@author: zil20
"""

def short(l):
    i = 0
    result = list()
    while (len(l[i]) <= 10) & (i < len(l)): 
        result.append(l[i])
        i += 1
    return result

print(short(['', '1'*11]))
print(short(['', '1'*10, '1'*11]))