# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:57:19 2018

@author: Administrator
"""

from urllib import request,parse
import json

#Form表单的数据要放到字典中,然后再进行编码转换
word = input("enter:")
data = {
	"i":word,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"1536648425867",
	"sign":"fd619fd54abf5fd17957e4eeef79bc3b",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTIME",
	"typoResult":"false"
	}
#data->bytes数据类型
data = parse.urlencode(data).encode("utf-8")

#将http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 中的"_o"去掉
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla5.0/"}

req = request.Request(url,data=data,headers=headers)
res = request.urlopen(req)
#result为json格式的字符串
result = res.read().decode("utf-8")

result_dict = json.loads(result)
translate = result_dict['translateResult'][0][0]['tgt']

print("translate:",translate)