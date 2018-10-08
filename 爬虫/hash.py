# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:10:44 2018

@author: Administrator
"""

import hashlib
#创建MD5的HASH对象
hashObj = hashlib.sha256()
sign = "HelloWorld"
#将字符串转成bytes,用update进行HASH
help(hashObj.update(sign.encode('utf-8')))
print(hashObj.hexdigest())

import builtwith
print(builtwith.parse("http://www.sina.com.cn"))
