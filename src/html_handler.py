from asyncio import get_event_loop

from bs4 import BeautifulSoup

from .request import request


async def html_processing() -> None:
    product = str(input('Введите название продукта: '))
    soup = BeautifulSoup(await request(product), 'html.parser')
    for html in soup.select('div.offer-wrapper'):
        title = html.select('a.marginright5.link.linkWithHash.detailsLink>strong')
        price = html.select('p.price>strong')
        data = html.select('small.breadcrumb.x-normal>span')

        print(f'''
Название товара: {title},
Цена товара: {price},
Дата публикации: {data}
        ''')


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(html_processing())