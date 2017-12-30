# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:39:58 2017

@author: zil20
"""

fname = input('Enter the file name: ')
fhandle = open(fname)
target = 'X-DSPAM-Confidence:'
count = 0
total = 0
for line in fhandle:
    if not line.startswith(target):
        continue
    line = line.rstrip()
    count += 1
    total += float(line[len(target):])
print('Average spam confidence:', total/count)