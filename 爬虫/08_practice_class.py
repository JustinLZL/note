# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:24:30 2018

@author: Administrator
"""

import urllib.request
import urllib.parse

class BaiduSpider:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}
    
    #请求并读取页面内容
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html      
    
    def writePage(self,filename,html):
        with open(filename,'w',encoding="utf-8") as f:
            f.write(html)
    
    def workOn(self):
        name = input("name of tieba:")
        begin = int(input("begin page:"))
        end = int(input("end page:"))
        kw={"kw":name}
        kw_str=urllib.parse.urlencode(kw)  
        for page in range(begin,end+1):
            pn = (page-1)*50
            url = self.baseurl+kw_str+"&pn="+str(pn)
            print("正在下载第%d页" % page)
            html = self.getPage(url)
            filename = "第"+str(page)+"页.html"
            self.writePage(filename,html)
            print("下载第%d页成功" % page)
            print('*'*30)
    
if __name__ == "__main__":
    spider = BaiduSpider()
    spider.workOn()