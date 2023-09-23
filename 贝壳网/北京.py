from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://bj.fang.ke.com/loupan/')

driver.implicitly_wait(10)

lis = driver.find_elements(By.CSS_SELECTOR, value='ul.resblock-list-wrapper > li')
for li in lis:
    try:
        names = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-name > a').text  # 楼盘名称
        sale = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-name > span').text  # 是否在售
        types = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-name > span:nth-child(3)').text  # 类型
        address = li.find_element(By.CSS_SELECTOR, value='div > a.resblock-location').text  # 地址
        measure = li.find_element(By.CSS_SELECTOR, value='div > a.resblock-room > span.area').text  # 面积
        adviser = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-agent > div > div > div > span').text  # 顾问
        label = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-tag > span:nth-child(1)').text  # 顾问
        price = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-price > div.main-price > span.number').text  # 价格
        average = li.find_element(By.CSS_SELECTOR, value='div > div > div.resblock-price > div.main-price > span.desc').text  # 均价
        asts = li.find_element(By.CSS_SELECTOR, value='div > div.resblock-price > div.second').text  # 一套
        prices = price + average
        print(names, sale, types, address, measure, adviser, label, prices, asts)
    except:
        print('出错了')
