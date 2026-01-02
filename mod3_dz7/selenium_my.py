from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import sqlite3

driver = webdriver.Chrome()
driver.get('https://www.olx.ua/uk/')
olx_in = driver.find_element(By.ID, 'search')
olx_in.send_keys('Мобильный телефон apple')
time.sleep(2)
olx_in.send_keys(Keys.ENTER)
time.sleep(2)

conn = sqlite3.connect('phones.db')
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS apple (id INTEGER PRIMARY KEY AUTOINCREMENT,
    description text not null,
    url text not null,
    price real not null)
    ''')
prices_elements = driver.find_elements(By.CSS_SELECTOR, 'p[data-testid="ad-price"]')

for element in prices_elements:
    text = element.text

    price_digits = ''.join(c for c in text if c.isdigit())
    if not price_digits:
        continue

    all_price = float(price_digits)
    # Делаем фильтр вывода. Больше 10 тыс, чтобы отсеять мусор
    if all_price > 10000:
        print(all_price)
        parent_div = element.find_element(By.XPATH, "./parent::div")
        link_elem = parent_div.find_element(By.TAG_NAME, 'a')

        url = link_elem.get_attribute('href')
        description = link_elem.text
        # Добавление в нашу таблицу
        cursor.execute(
            """
            INSERT INTO apple (description, url, price)
            VALUES (?, ?, ?)
            """,
            (description, url, all_price)
        )
        conn.commit()
