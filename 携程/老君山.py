import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

f = open('laojunshan.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['名字', '评论', '时间'])

csv_writer.writeheader()  # 写入表头

driver = webdriver.Chrome()
driver.get('https://you.ctrip.com/sight/shennongjia147/9298.html')

driver.implicitly_wait(2)


def get_job_info():
    lis = driver.find_elements(By.CSS_SELECTOR, value='.commentItem')
    for li in lis:
        name = li.find_element(By.CSS_SELECTOR, value='.userName').text
        title = li.find_element(By.CSS_SELECTOR, value='.commentDetail').text
        times = li.find_element(By.CSS_SELECTOR, value='.commentTime').text
        # print(name, title, times)
        dit = {
            '名字': name,
            '评论': title,
            '时间': times,
        }
        csv_writer.writerow(dit)
    driver.find_element(By.CSS_SELECTOR, value='.ant-pagination-next').click()


for page in range(4):
    time.sleep(2)
    get_job_info()


driver.quit()  # 自动关闭浏览器
