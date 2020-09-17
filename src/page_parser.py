from typing import List

from bs4 import BeautifulSoup

from .request import Request


class PageParser:
    def __init__(self, request: Request):
        self.request = request

    async def page_parse(self):
        soup = BeautifulSoup(await self.request.request('кролик'), 'lxml')
        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            a = pages.select_one('a')
            if a is None:
                a = None
            else:
                b = pages.select_one('a')['href']
                print(b)
