# -*- coding: utf-8 -*-
import requests
from lxml import etree
import pymongo

class QiushiSpider():
    def __init__(self):
        self.url = "https://www.qiushibaike.com/8hr/page/1"
        self.headers = {"User-Agent":"Mozilla5.0/"}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Baike
        self.myset = self.db.baiketab
    
    def getPage(self):
        res = requests.get(self.url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        #baseXpath
        base_list = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        for children in base_list:
            user_name = children.xpath('./div/a/h2')[0].text
            content = children.xpath('.//div[@class="content"]/span')[0].text
            likes = children.xpath('.//i')[0].text
            chat = children.xpath('.//i')[1].text
            d = {
                "user_name":user_name.strip(),
                "content":content.strip(),
                "likes":likes.strip(),
                "chat":chat.strip()
                }
            self.myset.insert(d)
        
    
if __name__ == "__main__":
    spider = QiushiSpider()
    spider.getPage()