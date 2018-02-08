import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("file:/home/jizong/Desktop/SpiderBook/ch09/9.4.4.login.html")

username = driver.find_element_by_name('username')
password = driver.find_element_by_xpath(".//*[@id='loginForm']/input[2]")
login_button = driver.find_element_by_xpath("//input[@type='submit']")

username.send_keys('qiye')
time.sleep(1)
password.send_keys('123')
time.sleep(1)
login_button.click()