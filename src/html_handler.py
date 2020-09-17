from typing import List

from bs4 import BeautifulSoup

from .request import Request


class HtmlHandler:
    def __init__(self, request: Request):
        self.request = request

    async def html_processing(self) -> List[str]:
        # product = str(input('Ведите название продукта: '))
        links = []
        soup = BeautifulSoup(await self.request.request('квартира'), 'lxml')
        for html in soup.select('div.offer-wrapper'):
            url = html.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']
            links.append(url)
        return links
