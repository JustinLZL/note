# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:05:55 2018

@author: Administrator
"""

class StackWithQueues:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def push(self,e):
        return self.s1.append(e)
    
    def pop(self):
        if len(self.s2)==0:
            while len(self.s1)>1:
                t = self.s1.pop(0)
                self.s2.append(t)
            self.s1,self.s2 = self.s2,self.s1
        return self.s2.pop(0)            
    
s = StackWithQueues()
s.push("a")
s.push("b")
s.push("c")
print(s.pop())
print(s.pop())
print(s.pop())