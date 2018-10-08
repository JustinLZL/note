# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:41:59 2018

@author: Administrator
"""

import re

s = '''<div><p>仰天大笑出门去,我辈岂是蓬蒿人</p></div>
<div><p>天生我材必有用,千金散去还复来</p></div>'''

#创建编译对象,贪婪匹配
p1 = re.compile('<p>(.*)</p>',re.S)#re.S使得'.'可以匹配'\n'
result1 = p1.findall(s)

#非贪婪匹配
p2 = re.compile('<p>(.*?)</p>',re.S)
result2 = p2.findall(s)

print("贪婪:",result1,"\n非贪婪:",result2)