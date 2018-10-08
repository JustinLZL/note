# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:28:29 2018

@author: Administrator
"""

#有10个球,颜色为黑/白
#用递归的方法把球的颜色可能性打印出来

count = 0
def perm(n,begin,end):
    global count
    if begin == end:#基准点
        print(n)
        count += 1
    else:
        perm(n,begin+1,end)
        n[begin] = (n[begin]+1)%2
        perm(n,begin+1,end)
        
L=[0,0,0,0,0,0,0,0,0,0]
perm(L,0,len(L))
print(count)