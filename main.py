import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#Add your sitemap in sitemap_url
sitemap_url = 'https://letsappit.com/sitemap.xml'


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
driver = webdriver.Firefox(options=firefox_options)
#driver = webdriver.Chrome()

response = requests.get(sitemap_url)

if response.status_code == 200:
    sitemap_content = response.text
    soup = BeautifulSoup(sitemap_content, 'lxml')

    urls = soup.find_all('loc')

    for url in urls:
        driver.get(url.text)
        time.sleep(100)

driver.quit()