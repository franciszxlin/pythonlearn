# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:33:15 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    print(line.rstrip().upper())    