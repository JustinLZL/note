# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:02:46 2018

@author: Administrator
"""

import urllib.request

url = "http://www.baidu.com/"
proxy = {"HTTP":"192.168.1.123:3128"}

proxy_handler = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_handler)
req = urllib.request.Request(url)
res = opener.open(req)

print(res.read().decode("utf-8"))