# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:13:36 2018

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
timedict = dict()
for line in fhand: 
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 3: continue
    time = words[5]
    h, m, s = time.split(":")
    timedict[h] = timedict.get(h, 0) + 1
t = list()
for item in timedict.items(): 
    t.append(item)
t.sort()
for i in t: 
    print(i[0], i[1])

