from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()
driver.get('https://detail.tmall.com/item.htm?spm=a230r.1.14.23.387e4e4cvv8d5A&id=669636819068&ns=1&abbucket=1')


# 设置一个向下滑动的操作
def drop_down():
    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver.find_element(By.CSS_SELECTOR, value='#login > div.corner-icon-view.view-type-qrcode > i').click()
driver.implicitly_wait(50)
driver.find_element(By.CSS_SELECTOR, value='#J_TabBar > li:nth-child(2)').click()


def get_shop():
    drop_down()
    lis = driver.find_elements(By.CSS_SELECTOR, value='#J_Reviews > div > div.rate-grid > table > tbody > tr')
    for li in lis:
        try:
            price = li.find_element(By.CSS_SELECTOR,
                                    value='td.tm-col-master > div.tm-rate-content > div.tm-rate-fulltxt').text
            style1 = li.find_element(By.CSS_SELECTOR, value=' td.col-meta > div.rate-sku > p:nth-child(1)').text
            style2 = li.find_element(By.CSS_SELECTOR, value=' td.col-meta > div.rate-sku > p:nth-child(2)').text
            style = style1 + style2
            print(price, style)
        except:
            continue


for page in range(1, 11):
    print(f'========正在采集第{page}页的数据内容========')
    time.sleep(2)
    get_shop()  # 采集一页数据后点击下一页
    for i in range(6, 100):
        driver.find_element(By.CSS_SELECTOR, value=f'#J_Reviews > div > div.rate-page > div > a:nth-child({i})').click()

