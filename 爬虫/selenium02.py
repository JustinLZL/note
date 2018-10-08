# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:53:07 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")

#driver.find_element_by_id("kw").send_keys(u"美女")
#driver.save_screenshot("输入美女.png")
#driver.find_element_by_id("su").click()
#time.sleep(3)
#driver.save_screenshot("搜索美女.png")

#r1 = driver.page_source.find("kw")
#r2 = driver.page_source.find("aaaaaaaaaaaaa")
#print(r1,r2)

result = driver.find_element_by_id("setf").text
print(result)