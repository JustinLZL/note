import requests

'''
request with cookies
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

cookies_str = ''
cookies_dict = {}
cookies_lst = cookies_str.split(';')
for cookie in cookies_lst:
    cookies_dict[cookie.split('=')[0]] = cookie.split('=')[1]

# 字典推导式
cookies_dict = {
    cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies_str.split(';')
}


# session类可以自动保存cookies，类似于cookiejar
session = requests.session()
# 1.代码模拟登录
login_url = ''
login_info = {
    '':'',
    '':''
}

login_response = session.post(login_url,
headers=headers,
data=login_info)
# 2.登录成功之后带着有效的cookies访问目标链接
person_url = '' #会员页

data = session.get(person_url, headers=headers)


