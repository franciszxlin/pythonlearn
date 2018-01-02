# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:29:26 2018

@author: zil20
"""

import string
fname = input('Enter a file name: ')
fhand = open(fname)
counts = dict()
for line in fhand: 
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words: 
        counts[word] = counts.get(word, 0) + 1
lst = list()
for k, v in counts.items(): 
    lst.append((v, k))
lst.sort(reverse = True)
for v, k in lst[:10]: 
    print(k, v)
    
    
    