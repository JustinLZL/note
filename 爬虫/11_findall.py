# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:58:14 2018

@author: Administrator
"""

import re

s = "A B C D"
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))