from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


def selenium_html() -> None:
    product = str(input('Введите товар который хотите искать: '))
    driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
    driver.get("https://www.olx.kz/kokshetau/q-" + product + '?page=2')
    # elem = driver.find_element_by_name("q")
    # elem.send_keys(product)
    # elem.send_keys(Keys.RETURN)
    # elem.click()
    assert "No results found." not in driver.page_source
    print(driver.page_source)
    time.sleep(5)
    driver.close()


selenium_html()
