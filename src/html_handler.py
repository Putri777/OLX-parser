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
            # title = html.select_one('a.marginright5.link.linkWithHash.detailsLink strong').get_text()
            # price = html.select_one('p.price>strong').get_text()
            # data = html.select_one('small.breadcrumb.x-normal>span').get_text()
    #         print(f'''
    # Название товара: {title},
    # Цена товара: {price},
    # Дата публикации: {data},
    # Ссылка на товар: {url}
    #         ''')

        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            a = pages.select_one('a')
            if a is None:
                a = None
            else:
                b = pages.select_one('a')['href']
                print(b)
        return links
