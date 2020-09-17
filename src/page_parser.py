from typing import List

from bs4 import BeautifulSoup

from .request import Request


class PageParser:
    def __init__(self, request: Request):
        self.request = request

    async def page_parse(self):
        soup = BeautifulSoup(await self.request.request('квартиры'), 'lxml')
        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                b = pages.select_one('a')['href'] if pages.select_one('a')['href'] is not None else None
                print(b)
            except TypeError as ex:
                # 'NoneType' object is not subscriptable
                pass
