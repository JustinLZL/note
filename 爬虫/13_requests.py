# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:24 2018

@author: Administrator
"""

import requests

url = "https://b-ssl.duitang.com/uploads/item/201503/28/20150328195003_ix5dW.jpeg"
headers = {"User-Agent":"Mozillea5.0/"}

response = requests.get(url,headers=headers)
#改变编码方式
response.encoding = "utf-8"


#print(response.encoding)

#print(response.text)



with open("czym.jpg",'wb') as f:
    f.write(response.content)