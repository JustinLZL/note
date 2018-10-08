# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:19:31 2018

@author: Administrator
"""

import requests

url = "http://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla5.0/"}
s = input('enter:')
wd = {"wd":s}

response = requests.get(url,params=wd,headers=headers)

response.encoding="utf-8"
print(response.text)