# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:42:57 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
worddict = {}
for line in fhand:
    words = line.split()
    for word in words:
        if word in worddict: continue
        worddict[word] = None
print(worddict)
            