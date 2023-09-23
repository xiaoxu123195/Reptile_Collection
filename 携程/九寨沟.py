import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

f = open('jiuzhaigou.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['id', '评分', '评论', '时间'])

csv_writer.writeheader()  # 写入表头

driver = webdriver.Chrome()
driver.get('https://you.ctrip.com/sight/jiuzhaigou25/77380.html')

driver.implicitly_wait(8)


def get_job_info():
    lis = driver.find_elements(By.CSS_SELECTOR, value='.commentItem')
    for li in lis:
        name = li.find_element(By.CSS_SELECTOR, value='.userName').text
        average = li.find_element(By.CSS_SELECTOR, value='.averageScore').text
        comment = li.find_element(By.CSS_SELECTOR, value='.commentDetail').text
        times = li.find_element(By.CSS_SELECTOR, value='.commentTime').text
        # tools = li.find_element(By.CSS_SELECTOR, value='.toolsItem').text
        # print(name, average, comment, times)
        dit = {
            'id': name,
            '评分': average,
            '评论': comment,
            '时间': times,
        }
        csv_writer.writerow(dit)
    # element1 = driver.find_element(By.CSS_SELECTOR, value='.ant-pagination-next')
    # driver.execute_script("arguments[0].click();", element1)
    driver.find_element(By.CSS_SELECTOR, value='.ant-pagination-next').click()


for page in range(101):
    time.sleep(2)
    get_job_info()

driver.quit()  # 自动关闭浏览器
