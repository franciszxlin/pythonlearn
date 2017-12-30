# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:30:16 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
wordsList = list()
for line in fhand:
    words = line.split()
    for word in words: 
        if word in wordsList: continue
        wordsList.append(word)
wordsList.sort()
print(wordsList)
    