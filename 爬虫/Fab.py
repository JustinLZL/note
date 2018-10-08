# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:16:37 2018

@author: Administrator
"""


def Fab(n):
    index,a,b = 0,0,1
    while index < n:
        a,b=b,a+b
        index +=1
        yield a

for i in Fab(10):
    print(i)
    
