# -*- coding: utf-8 -*-
import requests
import re

class NoteSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla5.0"}
        self.auth = ("tarenacode","code_2013")
        self.url = "http://code.tarena.com.cn/"
    
    def getParsePage(self):
        res = requests.get(self.url,auth=self.auth,headers=self.headers)
        res.encoding="utf-8"
        html = res.text
        p = re.compile('<a href="\w+/">(.*?)</a>',re.S)
        r_list = p.findall(html)
        self.writePage(r_list)
    
    def writePage(self,r_list):
        for r_str in r_list:
            with open("notebook.txt",'a') as f:
                f.write(r_str+'\n')
        print("done.")
    
    
if __name__ == "__main__":
    spider = NoteSpider()
    spider.getParsePage()