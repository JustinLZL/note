# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:43:41 2018

@author: Administrator
"""
from bs4 import BeautifulSoup

html="<div>九霄龙吟惊天变,风云际会浅水游</div>"
soup = BeautifulSoup(html,'lxml')

result = soup.div.string
print(result)