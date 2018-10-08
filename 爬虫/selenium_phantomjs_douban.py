# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:52:24 2018

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("https://www.zhihu.com/signup?next=%2F")
username = driver.find_element_by_name("username").send_keys('15521032797')

time.sleep(2)
driver.save_screenshot("zhihu.png")
