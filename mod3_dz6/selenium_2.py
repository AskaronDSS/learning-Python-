from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
driver = webdriver.Edge()

try:
    # Navigate to the target page
    driver.get("https://www.olx.ua/uk/")
    print(f"Navigated to: {driver.current_url}")

    time.sleep(2) 
    print(f"New page URL: {driver.current_url}")

    

    submit_button = driver.find_element(By.ID, 'search')
    print(submit_button)
    submit_button.send_keys('Оперативка ДДР5')
    time.sleep(1)
    submit_button.click()
    time.sleep(2)

    press_button = driver.find_element(By.NAME, 'searchBtn')
    press_button.click()
    time.sleep(5)


    prices_elements = driver.find_elements(By.CSS_SELECTOR,'p[data-testid="ad-price"]')
    for element in prices_elements:
        price_string = element.text.replace(' ','')
        search_price = re.search('\d+', price_string).span()
        all_price = float(price_string[search_price[0]:search_price[1]])
        if all_price < 10000:
            parent_div = element.find_element(By.XPATH, "./parent::div")
            link_elem = parent_div.find_element(By.TAG_NAME,'a')
            url = link_elem.get_attribute('href')
            driver.get(url)
            break
    time.sleep(10)

    # link_element2 = driver.find_element(By.ID, ':r0:')
    # link_element2.clear()
    # link_element2.send_keys('123@gmail.com')

    # link_pass = driver.find_element(By.ID, ':r1:')
    # link_pass.clear()
    # link_pass.send_keys('123123123')

    # print(f'link_element2 -> {link_element2}')


    # Wait for the link to be clickable (good practice for dynamic elements)
    # The link text on example.com is "More information..."
    # link_text = "My LMS"
    # link_element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.LINK_TEXT, link_text))
    # )
    
    # print(f"Found the link with text: '{link_text}'")

    # Click the link
    # link_element.click()
    # print("Link clicked.")

    # Optional: Verify the new URL or wait to observe the result
    

    # id_text = ":r0:"
    
    # link_element2.clear()
    # link_element2.send_keys("Hello, world!")
    

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    # driver.quit()
    pass