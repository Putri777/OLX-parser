from typing import List

from bs4 import BeautifulSoup

from .request import Request


class HtmlHandler:
    def __init__(self, request: Request) -> None:
        """
        Constructor takes one parameter `request`
        :param request: Request
        """
        self.request = request

    async def html_processing(self) -> List[str]:
        """
        The method returns links to the  product in the List
        :return: List[str]
        """
        product = str(input('Ведите название продукта: '))
        links = []
        soup = BeautifulSoup(await self.request.request(product), 'lxml')
        for html in soup.select('div.offer-wrapper'):
            url = html.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']
            links.append(url)
        return links

    async def page_processing(self, links):
        page = await self.browser.get_html(links)
        soup = BeautifulSoup(page, 'lxml')
        title = await soup.select_one('div.offer-titlebox>h1').get_text()
        price = await soup.select_one('strong.pricelabel__value.not-arranged').get_text()
        description = await soup.select_one('div.clr.lheight20.large').get_text()
        phone = await soup.select_one('div.contactitem>strong').get_text()
        print(title, price, description, price, phone)