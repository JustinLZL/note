# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:02:29 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

url = "http://www.baidu.com/s?wd="
key = input('enter:')
wd = urllib.parse.quote(key)
url += wd

headers={"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")

print(html)