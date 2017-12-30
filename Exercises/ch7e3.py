# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:56:57 2017

@author: zil20
"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count += 1
    print('There were', count, 'subject lines in', fname)
except: 
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened:', fname)