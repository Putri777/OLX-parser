from typing import Dict

from aiohttp import ClientSession


class Request:
    def __init__(self, user_agent: Dict, product: str) -> None:
        self.user_agent = user_agent
        self.product = product

    async def request(self) -> str:
        session = ClientSession()
        async with session.get(headers=self.user_agent,
                               url=f'https://www.olx.kz/kokshetau/q-{self.product}') as response:
            content = await response.text()
        await session.close()

        return content
