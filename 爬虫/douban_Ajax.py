# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:26:03 2018

@author: Administrator
"""

import requests
import json
import csv

#该路径由Fiddler抓包
url = "https://movie.douban.com/j/chart/top_list/"
params = {
        "type":"11",
        "interval_id":"100:90",
        "action":"",
        "start":"0",
        "limit":"100"
        }
headers = {"User-Agent":"Mozilla5.0/"}

res = requests.get(url,params=params,headers=headers)
res.encoding="utf-8"
html = res.text
L = json.loads(html)
for film in L:
    score = film['rating'][0]
    name = film['title']
    
    with open("douban100.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name,score])

print("End.")
