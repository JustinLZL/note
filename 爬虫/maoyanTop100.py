# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:50:23 2018

@author: Administrator
"""

import random
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager
import functools
import basicSpider
import myPymysql

count = 0
def write2Sql(item):
    global count
    count += 1
    sqlHelper = myPymysql.DBHelper()
    title = item['title']
    actor = item['actor']

def write2File(item):
    with open('猫眼电影2.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')

def parseOnePage(html):
    pattern = re.compile('<div class="movie-item-info">[\s\S]*?<p class="name"><a href="/films/[\s\S]*?" title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>[\s\S]*?</div>')
    results = re.findall(pattern,html)
    for it in results:
        yield{"title":it[0].strip(),
              "actor":it[1].strip(),
              "releasetime":it[2].strip()}
    
def CrawlMovieInfo(lock,offset, ua='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'):
    '''
    抓取猫眼电影数据
    '''
    #抓取页面
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    headers = [("User-Agent",ua)]   
    html = basicSpider.downloadHtml(url, headers=headers)
    #抓取内容,存储
    for item in parseOnePage(html):
        lock.acquire()
        write2File(item)
        lock.release()

if __name__ == "__main__":
    #L = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    #     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    #     "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    #        ]
#    for i in range(10):
#        CrawlMovieInfo(url+str(i*10),ua=random.choice(L))
    
    #需要使用进程池来操作lock
    manager = Manager()
    lock = manager.Lock()
    
    #functools将原函数进行包装,进行传lock
    partial_CrawlMovieInfo=functools.partial(CrawlMovieInfo,lock)
    pool = Pool()
    pool.map(partial_CrawlMovieInfo,[i*10 for i in range(10)])
    pool.close()
    pool.join()
    
    print('over')