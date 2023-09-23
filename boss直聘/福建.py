import time

from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

f = open('data01.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['职务', '地区', '公司名字', '薪资', '经验', '公司类型', '公司福利'])

csv_writer.writeheader()  # 写入表头

# 实例化浏览器对象
driver = webdriver.Chrome()
driver.get('https://www.zhipin.com/job_detail/?query=%E7%A6%8F%E5%BB%BA&city=100010000&industry=&position=')

driver.implicitly_wait(10)  # 隐式等待


# time.sleep(10) 死等 一定要等够10秒 才进行下一步操作
# driver.find_element_by_css_selector('.ipt-search').send_keys('福建')
# driver.find_element_by_css_selector('button.btn.btn-search').click()

# 通过两次提取，第一次获取所有的li标签内容
# lis = driver.find_elements_by_css_selector('.job-list li')

def get_job_info():
    lis = driver.find_elements(By.CSS_SELECTOR, value='.job-list li')

    for li in lis:
        # title = li.find_element_by_css_selector('.job-area').text
        area = li.find_element(By.CSS_SELECTOR, value='.job-area').text  # 地区
        title = li.find_element(By.CSS_SELECTOR, value='.job-name a').text  # 职务
        # href = li.find_element(By.CSS_SELECTOR, value='job-name a').get_attribute('href')  # 详情页
        # 字符串替换replace() remove 列表方法 strip() 去除字符串两端的空格
        company_name = li.find_element(By.CSS_SELECTOR, value='.company-text .name a').get_attribute('title').replace(
            '招聘', '')  # 公司名字
        money = li.find_element(By.CSS_SELECTOR, value='.job-limit .red').text  # 薪资
        exp = li.find_element(By.CSS_SELECTOR, value='.job-limit p').text  # 经验学历
        company_type = li.find_element(By.CSS_SELECTOR, value='.false-link').text  # 公司类型
        company_boon = li.find_element(By.CSS_SELECTOR, value='.info-desc').text  # 公司福利
        dit = {
            '职务': title,
            '地区': area,
            '公司名字': company_name,
            '薪资': money,
            '经验': exp,
            '公司类型': company_type,
            '公司福利': company_boon,
        }
        csv_writer.writerow(dit)
        # print(title, area, company_name, money, exp, company_type, company_boon)
    driver.find_element(By.CSS_SELECTOR, value='.next').click()


for page in range(1):
    time.sleep(2)
    get_job_info()


driver.quit()  # 自动关闭浏览器
