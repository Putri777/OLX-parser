from typing import List

from bs4 import BeautifulSoup

from .request import Request


class PageParser:
    def __init__(self, request: Request):
        self.request = request

    async def page_parse(self) -> List:
        product = str(input('Ведите название продукта: '))
        pages_list = []
        soup = BeautifulSoup(await self.request.request(product), 'lxml')
        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                pages_list.append(pages.select_one('a')['href'] if pages.select_one('a')['href'] is not None else None)
            except TypeError as ex:
                # 'NoneType' object is not subscriptable
                pass

        return pages_list
