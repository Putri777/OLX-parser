from typing import Dict

from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


async def request() -> str:
    product = str(input('Введите название продукта: '))
    session = ClientSession()
    async with session.get(headers=user_agent, url=f'https://www.olx.kz/kokshetau/q-{product}') as response:
        content = await response.text()
    await session.close()

    return content


if __name__ == '__main__':
    loop = get_event_loop()
    # loop.run_until_complete(html_processing())
    print(loop.run_until_complete(request()))
