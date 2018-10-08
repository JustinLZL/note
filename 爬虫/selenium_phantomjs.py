# -*- coding: utf-8 -*-
#导入selenium库中的webdriver
from selenium import webdriver

#创建打开phantomjs的对象
driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com/")

#获取网页截图
driver.save_screenshot("baidu.png")