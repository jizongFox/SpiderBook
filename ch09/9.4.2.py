#coding:utf-8
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys("网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"网络爬虫." not in driver.page_source
driver.close()
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://train.trip.taobao.com/stsSearch.htm")
time.sleep(7)
assert "火车票预订" in driver.title
elem = driver.find_element_by_id("J_DepCity")
elem.clear()
# time.sleep(2)
elem.send_keys("德阳")
# time.sleep(2)
# elem.send_keys(Keys.DOWN)
time.sleep(1)
elem.send_keys(Keys.ENTER)

elem = driver.find_element_by_id("J_ArrCity")
elem.clear()
elem.send_keys("苏州")
# time.sleep(1)
# elem.send_keys(Keys.DOWN)
# time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(3)

elem = driver.find_element_by_id("J_depDate")
elem.clear()
elem.send_keys("2018-02-25")
# time.sleep(1)
# elem.send_keys(Keys.DOWN)
# time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(3)

elem = driver.find_element_by_class_name("search-field")
elem.click()
time.sleep(100)
# elem.clear()
# elem.send_keys("2018-2-25")
# time.sleep(1)
# # elem.send_keys(Keys.DOWN)
# # time.sleep(1)
# elem.send_keys(Keys.ENTER)



assert u"网络爬虫." not in driver.page_source
driver.close()
