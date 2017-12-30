# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:40:40 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
fcount = 0
for line in fhand:
    if not line.startswith('From'):  continue
    fcount += 1
    words = line.split()
    print(words[1])
print('There were', fcount, 'lines in the file with From as the first word')
    