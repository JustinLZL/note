# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:06:46 2018

@author: Administrator
"""

import hashlib

def hashStr(strInfo):
    '''
    对字符串进行hash
    '''
    hashObj = hashlib.sha256()
    hashObj.update(strInfo.encode('utf-8'))
    return hashObj.hexdigest()


#print(hashStr('hello'))
    

chunkSize = 2048
def hashFile(filename):
    hashObj = hashlib.sha256()
    with open(filename,'rb') as f:
        while True:
            #不能一次性读取文件所有内容
            #文件过大时,内存会不够
            chunk = f.read(chunkSize)
            if not chunk:
                break
            hashObj.update(chunk)
    return hashObj.hexdigest()


print(hashFile('baidu.png'))