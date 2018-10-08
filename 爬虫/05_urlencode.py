# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:17:16 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

url = "http://www.baidu.com/s?"
key = input('enter:')
dic = {"wd":key}
dic_str = urllib.parse.urlencode(dic)
url += dic_str
headers = {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}

requset = urllib.request.Request(url,headers = headers)
response = urllib.request.urlopen(requset)
html = response.read().decode("utf-8")

print(html)