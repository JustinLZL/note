# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:31:49 2018

@author: Administrator
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.PhantomJS()
driver.get("https://www.douyu.com/directory/all")

for i in range(10):
    #创建一个解析对象
    soup = bs(driver.page_source,"lxml")
    #调用方法查找元素
    names = soup.find_all('span',{'class':"dy-name ellipsis fl"})
    nums = soup.find_all('span',{'class':"dy-num fr"})
    
    for name,num in zip(names,nums):
        print("观众人数:",num.get_text().strip(),
              "\t主播名字:",name.get_text().strip())
        
    if driver.page_source.find("shark-pager-disable-next")== -1:
        driver.find_element_by_class_name("shark-pager-next").click()
    else:
        break