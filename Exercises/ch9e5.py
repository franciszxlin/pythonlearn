# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:51:50 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
domaindict = {}
for line in fhand:
    if not line.startswith('From:'): continue
    words = line.split()
    address = words[1]
    emailcomponent = address.split(sep='@')
    domain = emailcomponent[1]
    domaindict[domain] = domaindict.get(domain, 0) + 1 
print(domaindict)