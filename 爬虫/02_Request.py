# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:17:13 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
headers={"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}

#1.构建请求对象
request = urllib.request.Request(url,headers=headers)
#2.获取响应对象
response = urllib.request.urlopen(request)
#3.获取响应对象内容
html = response.read().decode("utf-8")

#获取响应码
print(response.getcode())
#获取响应报头信息
print(response.info())