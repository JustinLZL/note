# -*- coding: utf-8 -*-
import urllib.request

server = "192.168.1.123:3128"
user = "309435365"
password = "szayclhp"
url = "http://www.baidu.com/"

pwd = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd.add_password(None,server,user,password)
pwd.add_password(None,"http://code.tarena.com.cn/","tarenacode","code_2013)

proxy_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(proxy_handler)

req = urllib.request.Request(url)
res = opener.open(req)
html = res.read().decode("utf-8")
print(html)