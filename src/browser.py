import time
from asyncio import run, get_event_loop

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .html_handler import HtmlHandler
from .request import Request

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


class Browser:
    def __init__(self):
        pass

    async def get_html(self, links: list):
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for x in links:
            driver.get(x)
            elem = driver.find_element_by_css_selector('strong.xx-large')
            elem.click()
            print(driver.page_source)
            driver.close()

async def main():
    request = Request(user_agent)
    html_handler = HtmlHandler(request)
    a = Browser()
    await a.get_html(await html_handler.html_processing())

if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(main())

