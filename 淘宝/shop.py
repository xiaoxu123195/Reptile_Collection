from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

f = open('商品.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '价格',
    '标签',
    '详情',
    '付款',
    '店铺',
])
csv_writer.writeheader()

driver = webdriver.Chrome()
driver.get('https://www.taobao.com/')


# 设置一个向下滑动的操作
def drop_down():
    for x in range(1, 12, 2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver.find_element(By.CSS_SELECTOR, value='#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h').click()
driver.find_element(By.CSS_SELECTOR, value='#login > div.corner-icon-view.view-type-qrcode > i').click()
driver.implicitly_wait(50)
driver.find_element(By.CSS_SELECTOR, value='#q').send_keys('平板')
driver.find_element(By.CSS_SELECTOR, value='#J_TSearchForm > div.search-button > button').click()
driver.implicitly_wait(10)


def get_shop():
    lis = driver.find_elements(By.CSS_SELECTOR, value='#mainsrp-itemlist > div > div > div:nth-child(1) > div')
    for li in lis:
        try:
            price = li.find_element(By.CSS_SELECTOR, value='div.price > strong').text
            title = li.find_element(By.CSS_SELECTOR, value='div.row.row-2.title > a').text
            href = li.find_element(By.CSS_SELECTOR, value='div.row.row-2.title > a').get_attribute('href')
            evaluate = li.find_element(By.CSS_SELECTOR, value=' div.row > div.deal-cnt').text
            shop = li.find_element(By.CSS_SELECTOR, value='div.row > div.shop > a > span:nth-child(2)').text
            # print(price, title, href, evaluate, shop)
            dit = {
                '价格': price,
                '标签': title,
                '详情': href,
                '付款': evaluate,
                '店铺': shop,
            }
            csv_writer.writerow(dit)
        except:
            print('有些商品没有店铺，数据缺失，跳过')


for page in range(1, 11):
    print(f'========正在采集第{page}页的数据内容========')
    time.sleep(3)
    get_shop()  # 采集一页数据后点击下一页
    driver.find_element(By.CSS_SELECTOR, value=' li.item.next > a > span.icon.icon-btn-next-2').click()



