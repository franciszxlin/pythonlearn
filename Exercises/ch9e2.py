# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:05:14 2017

@author: zil20
"""

fname = input('Enter a file name: ')
fhand = open(fname)
# daydict = {}
# addressdict = {}
freqdict = {}
for line in fhand:
    if not line.startswith('From:'): continue
    words = line.split()
    address = words[1]
    freqdict[address] = freqdict.get(address, 0) + 1
t=list()
for address, freq in freqdict.items(): 
    t.append((freq, address))
t.sort(reverse=True)
print(t[0][1], t[0][0])
'''
    if len(words) < 3: continue
    day = words[2]
    daydict[day] = daydict.get(day, 0) + 1
print(daydict)
    address = words[1]
    addressdict[address] = addressdict.get(address, 0) + 1
addressdict1 = {k:int(addressdict[k]/2) for k in addressdict}
vlist = list(addressdict1.values())
maxvalue = max(vlist)
maxkey = [k for k, v in addressdict1.items() if v == maxvalue][0]
print(maxkey, maxvalue)
#print(addressdict1)
'''