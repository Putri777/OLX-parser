from selenium import webdriver


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
            except:
                pass
            print(driver.page_source)

