# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:53:24 2018

@author: Administrator
"""

import requests
import re


class duanzi():
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/article/index"
        self.page = 1
        self.headers = {"User-Agent":"Mozilla5.0/"}
    
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html = res.text
        self.parsePage(html)
    
    def parsePage(self,html):
       p = re.compile('<div class="desc">(.*?)</div>',re.S)
       r_list = p.findall(html)
       self.writePage(r_list)
    
    def writePage(self,r_list):
        for r_str in r_list:
            with open("duanzi.txt",'a') as f:
                r_str = r_str.strip().replace("　　",'')
                f.write(r_str+"\n\n")
    
    def handler(self):
        while True:
            if self.page == 1:
                url = self.baseurl+".html"
            else:
                url = self.baseurl+"_"+str(self.page)+".html"
            print("正在爬取第{}页".format(self.page))
            self.getPage(url)
            print("爬取第{}页成功".format(self.page))
            
            c = input("是否继续爬取?(y/n):")
            if c == "y":
                self.page+=1
            else:
                print("end.")
                break
    
if __name__ == "__main__":
    spider = duanzi()
    spider.handler()