from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

f = open('商品.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '价格',
    '标签',
    '详情',
    '评价数',
    '店铺',
])
csv_writer.writeheader()

driver = webdriver.Chrome()
driver.get('https://www.jd.com/')


# 设置一个向下滑动的操作
def drop_down():
    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver.find_element(By.CSS_SELECTOR, value='#key').send_keys('平板')
driver.find_element(By.CSS_SELECTOR, value='#search > div > div.form > button').click()
driver.implicitly_wait(10)


def get_shop():
    drop_down()  # 调用函数
    lis = driver.find_elements(By.CSS_SELECTOR, value='.gl-item')
    for li in lis:
        try:
            price = li.find_element(By.CSS_SELECTOR, value='div > div.p-price > strong > i').text
            title = li.find_element(By.CSS_SELECTOR, value='div > div.p-name.p-name-type-2 > a > em').text
            href = li.find_element(By.CSS_SELECTOR, value='div > div.p-name.p-name-type-2 > a').get_attribute('href')
            evaluate = li.find_element(By.CSS_SELECTOR, value='div > div.p-commit > strong > a').text + '条评价'
            shop = li.find_element(By.CSS_SELECTOR, value='div > div.p-shop > span > a').text
            dit = {
                '价格': price,
                '标签': title,
                '详情': href,
                '评价数': evaluate,
                '店铺': shop,
            }
            csv_writer.writerow(dit)
            # print(price, title, href, evaluate, shop)
        except:
            print('有些商品没有店铺，数据缺失，跳过')


for page in range(1, 11):
    print(f'========正在采集第{page}页的数据内容========')
    get_shop()  # 采集一页数据后点击下一页
    driver.find_element(By.CSS_SELECTOR, value='.pn-next').click()
