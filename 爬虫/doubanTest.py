# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:24:09 2018

@author: Administrator
"""


crawl_queue = [] #待爬队列
crawled_queue = []

def CrawlMovieInfo(url):
    global crawl_queue
    global crawled_queue
    
    html = get_html(url)
    