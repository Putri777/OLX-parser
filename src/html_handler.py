from asyncio import get_event_loop

from bs4 import BeautifulSoup

from .request import request


async def html_processing() -> None:
    product = str(input('Введите название продукта: '))
    soup = BeautifulSoup(await request(product), 'lxml')
    for html in soup.select('div.offer-wrapper'):
        title = html.select_one('a.marginright5.link.linkWithHash.detailsLink strong').get_text()
        price = html.select_one('p.price>strong').get_text()
        data = html.select_one('small.breadcrumb.x-normal>span').get_text()
        url = html.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']

        print(f'''
Название товара: {title},
Цена товара: {price},
Дата публикации: {data},
Ссылка на товар: {url}
        ''')


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(html_processing())
