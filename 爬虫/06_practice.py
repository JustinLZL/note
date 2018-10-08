# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:59:56 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

baseurl = "http://tieba.baidu.com/f?"
headers = {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}

kw = input("name of tieba:")
begin = int(input("begin page:"))
end = int(input("end page:"))

#对URL进行编码
kw_dic = {"kw":kw}
kw_str = urllib.parse.urlencode(kw_dic)

for page in range(begin,end+1):
    pn = (page-1)*50
    url = baseurl + kw_str + "&pn=" + str(pn)
    #print(url)
    req = urllib.request.Request(url,headers = headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    filename = "第"+str(page)+"页.html"
    with open(filename,'w',encoding="utf-8") as f:
        print("正在下载第%d页" % page)
        f.write(html)
        print("第%d页下载成功" % page)
        print('*'*30)