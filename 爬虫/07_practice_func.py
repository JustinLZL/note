# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:40:56 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

#get HTML:send a requset and get a response
def getPage(url):
    headers = {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html
    
#save HTML to local
def writePage(filename,html):
    with open(filename,'w',encoding="utf-8") as f:
        f.write(html)

#main function
def workOn():
    name = input("name of tieba:")
    begin = int(input("begin page:"))
    end = int(input("end page:"))
    baseurl="http://tieba.baidu.com/f?"
    kw={"kw":name}
    kw_str=urllib.parse.urlencode(kw)  
    for page in range(begin,end+1):
        pn = (page-1)*50
        url = baseurl+kw_str+"&pn="+str(pn)
        print("正在下载第%d页" % page)
        html = getPage(url)
        filename = "第"+str(page)+"页.html"
        writePage(filename,html)
        print("下载第%d页成功" % page)
        print('*'*30)
    

if __name__ == "__main__":
    workOn()