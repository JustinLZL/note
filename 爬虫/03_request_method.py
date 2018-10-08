# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:33:15 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
headers = "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"

requset = urllib.request.Request(url)
#请求对象方法
requset.add_header("User-Agent",headers)
response = urllib.request.urlopen(requset)
#get_header()方法获取User-Agent
print(requset.get_header("User-agent"))