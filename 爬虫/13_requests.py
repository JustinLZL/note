import requests
import json

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

response = requests.get(url, headers = headers )

#返回状态码不是200时抛出异常
response.raise_for_status()


#content属性返回的是bytes类型
# data = response.content
#根据html页面头部中meta的charset类型来决定转码格式
#一般类型为gbk或utf-8
data = response.content.decode('utf-8')

# str->dict 
data_dict = json.loads(data)

# json()自动将json字符串转换为python dict/list
data = response.json()

#text属性返回的是str类型，但是转译可能会有问题
data = response.text

#请求头
request_headers = response.request.headers

#响应头
response_headers = response.headers

#响应状态码
response_code = response.status_code

#请求的cookie(有可能没有，取出来的都是cookiejar对象)
request_cookie = response.request._cookies  #<RequestsCookieJar[]>
# <RequestsCookieJar[<Cookie BAIDUID=C6577DE32355351076ABD5C7FE82E33A:FG=1 for .baidu.com/>, <Cookie BIDUPSID=C6577DE3235535101139AE25B7A08B9D for .baidu.com/>, <Cookie PSTM=1574336534 for .baidu.com/>, <Cookie BD_LAST_QID=16597857538657091036 for www.baidu.com/>]>

#响应的cookie
response_cookie = response.cookies  #<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# <RequestsCookieJar[<Cookie H_PS_PSSID=1444_21112_29567_29221 for .baidu.com/>, <Cookie delPer=0 for .baidu.com/>, <Cookie BDSVRTM=0 for www.baidu.com/>, <Cookie BD_HOME=0 for www.baidu.com/>]>


# 发送POST请求
response = requests.post(url, data=data)


# proxy代理
proxy = {
    'https':'ip:port',
    ...
}
response = requests.post(url, data=data, proxies=proxy)


