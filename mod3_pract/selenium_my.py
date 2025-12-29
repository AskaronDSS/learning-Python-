import re
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

import sqlite3

driver = webdriver.Chrome()
driver.get('https://www.olx.ua/uk/')
olx_in = driver.find_element(By.ID, 'search')
olx_in.send_keys('Мобильный телефон apple')
time.sleep(1)
olx_in.send_keys(Keys.ENTER)
time.sleep(3)

conn = sqlite3.connect('phones.db')
cursor = conn.cursor()

# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS apple (id int auto-increment primary key,
#     description text not null,
#     url text not null,
#     price text not null)
#     ''')

prices_elements = driver.find_elements(By.CSS_SELECTOR, 'p[data-testid="ad-price"]')
for element in prices_elements:
    price_string = element.text.replace(' ', '')
    search_price = re.search('\d+', price_string).span()
    all_price = float(price_string[search_price[0]:search_price[1]])
    if all_price > 10000:
        parent_div = element.find_element(By.XPATH, "./parent::div")
        link_elem = parent_div.find_element(By.TAG_NAME, 'a')
        url = link_elem.get_attribute('href')
        descrip = element.find_element(By.TAG_NAME, 'h4')
        print(descrip)

