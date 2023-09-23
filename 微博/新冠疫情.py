from bs4 import element
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import csv
import time


driver = webdriver.Chrome()
driver.get('https://weibo.com/')
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, value='div.woo-panel-main> div > button').click()
driver.implicitly_wait(50)
# driver.find_element(By.CSS_SELECTOR, value='span > form > div > .woo-input-main').send_keys('新冠疫情')
# element.send_keys(Keys.ENTER)



