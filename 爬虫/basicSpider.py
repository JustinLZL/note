# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 10:10:12 2018

@author: Administrator
"""
from urllib import request
from urllib import error
from urllib import parse
import random
import time

def downloadHtml(url , headers=[()] , proxy = {},
                timeout=None,decodeInfo="utf-8",
                num_tries=10,useProxyRatio=12):
    '''
    写一个完善一点的下载网页的逻辑
    支持User-Agent等Http Requset Headers
    支持Proxy
    超时的考虑
    编码的问题,如果不是utf-8编码怎么办
    服务器返回5xx怎么办
    客户端返回4xx怎么办
    考虑延时的问题
    '''
    #控制访问,不要太过频繁
    #time.sleep(random.randint(1,2))
    
    if random.randint(1,10)>useProxyRatio:
        proxy = None
        
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    #设置User-Agent
    opener.addheaders = headers
    request.install_opener(opener)
    
    html = None
    try:
        #编码异常
        #网络下载异常:客户端的异常404,403
                    #服务端的异常5xx
        res = request.urlopen(url)
        html = res.read().decode(decodeInfo)
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
    except error.URLError or error.HTTPError as e:
        #客户端的异常:403,404
        if hasattr(e,'code') and 400<=e.code<500:
            print('Client Error:'+e.code)
        elif hasattr(e,'code') and 500<=e.code<600:
            if num_tries > 0:
                time.sleep(random.randint(1,3))
                downloadHtml(url,
                             headers,
                             proxy,
                             timeout,
                             decodeInfo,
                             num_tries-1)
    
    return html
             
