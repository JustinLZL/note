# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:43:24 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
#发起请求并获取响应对象
response = urllib.request.urlopen(url)
#响应对象的read()方法获取响应内容(得到的是bytes类型)
html = response.read().decode("utf-8")
print(html)