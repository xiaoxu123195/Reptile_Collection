import requests
# 用来输出信息
import logging
import re
# 用来做url的拼接
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://ssr1.scrape.center/page/1'
TOTAL_PAGE = 10


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        print(response.text)
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


scrape_page(BASE_URL)
