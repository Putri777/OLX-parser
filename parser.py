from typing import Dict

from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup


user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
olx_link = 'https://www.olx.kz/kokshetau/q-%D0%BA%D1%80%D0%BE%D0%BB%D0%B8%D0%BA/'


async def request(headers: Dict, url: str) -> None:
    session = ClientSession()
    async with session.get(headers=headers, url=url) as response:
        content = await response.text()
        print(content)


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(request(user_agent, olx_link))

