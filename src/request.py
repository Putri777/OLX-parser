from typing import Dict

from aiohttp import ClientSession

# user_agent = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
# }


class Request:
    def __init__(self, user_agent: Dict, product: str) -> None:
        self.user_agent = user_agent
        self.product = product

    async def request(self) -> str:
        session = ClientSession()
        async with session.get(headers=self.user_agent, url=f'https://www.olx.kz/kokshetau/q-{self.product}') as response:
            content = await response.text()
        await session.close()

        return content
