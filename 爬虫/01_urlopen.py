import urllib.request
import urllib.parse
import string
import random

def get_params():
	url = 'http://www.baidu.com/s?'

	params = {
		'wd':'中文',
		'key':'lll'
	}

	str_params = urllib.parse.urlencode(params)
	print(str_params)

	final_url = url + str_params

	#将带有中文的url转译成计算机可识别
	end_url = urllib.parse.quote(final_url, safe=string.printable)

	response = urllib.request.urlopen(end_url)

	data = response.read().decode("utf-8")
	print(data)


def load_baidu():
	url = 'http://www.baidu.com'
	#添加请求头信息
	headers = {
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
		# 'user-name':'Justin'
	}
	
	#创建请求对象
	request = urllib.request.Request(url,headers=headers)
	#动态添加请求头信息
	request.add_header('user-name','Justin')
	#请求网络数据
	response = urllib.request.urlopen(request)
	print(response)
	data = response.read().decode("utf-8")
	# print(data)

	#响应头
	# print(response.headers)
	#获取请求头信息
	request_headers = request.headers
	print(request_headers)

	# 获取完整的url
	full_url = request.get_full_url()
	print(full_url)


def random_user_agent():
	url = 'http://www.baidu.com'
	user_agent_list = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
	]
	user_agent = random.choice(user_agent_list)

	request = urllib.request.Request(url)

	request.add_header("User-Agent",user_agent)

	response = urllib.request.urlopen(request)
	print(request.get_header("User-agent"))#注意大小写

if __name__ == "__main__":
	# get_params()
	# load_baidu()
	random_user_agent()

