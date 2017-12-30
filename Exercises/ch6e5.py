# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:33:09 2017

@author: zil20
"""

str = 'X-DSPAM-Confidence:0.8475'
bpos = str.find(':')
ext = float(str[bpos+1:])
print(ext)

