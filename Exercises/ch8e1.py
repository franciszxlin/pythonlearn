# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:07:42 2017

@author: zil20
"""

def chop(alist):
    alist.pop(0)
    alist.pop(len(alist)-1)
    return None

def middle(alist):
    return alist[1:len(alist)-1]

testlist = ['a', 'b', 'c', 'd']
# chop(testlist)
newlist = middle(testlist)
# print(testlist)
print(newlist)