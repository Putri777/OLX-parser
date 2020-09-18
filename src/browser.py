import time

from selenium import webdriver
from bs4 import BeautifulSoup


class Browser:
    def __init__(self):
        pass

    async def get_html(self, links):
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for x in links:
            driver.get(x)
            try:
                elem = driver.find_element_by_css_selector('span.button.inverted.spoiler')
                elem.click()
                time.sleep(0.2)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                title = soup.select_one('div.offer-titlebox>h1').get_text()
                price = soup.select_one('strong.pricelabel__value.not-arranged').get_text()
                description = soup.select_one('div.clr.lheight20.large').get_text()
                phone = soup.select_one('div.contactitem>strong').get_text()
                print(f'''
Название: {title}
Цена: {price}
Описание: {description}
Номер телефона: {phone}
Ссылка на товар: {x}
''')
            except:
                pass
            # print(driver.page_source)

    async def give_html(self, links):
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for x in links:
            driver.get(x)
            try:
                print('руыв')
                elem = driver.find_element_by_css_selector('span.button.inverted.spoiler')
                elem.click()
                time.sleep(0.2)
                return driver.page_source
                # soup = BeautifulSoup(driver.page_source, 'lxml')
            except:
                pass
        # return driver.page_source

