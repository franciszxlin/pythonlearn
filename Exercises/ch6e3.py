# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:11:24 2017

@author: zil20
"""

def count(string, letter):
    count = 0
    for eachLetter in string:
        if eachLetter == letter:
            count += 1
    return count

word = 'banana'
print(count(word, 'a'))