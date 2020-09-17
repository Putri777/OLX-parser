from typing import Dict

from aiohttp import ClientSession


class Request:
    def __init__(self, user_agent: Dict) -> None:
        self.user_agent = user_agent

    async def request(self, product: str) -> str:
        session = ClientSession()
        async with session.get(headers=self.user_agent,
                               url=f'https://www.olx.kz/kokshetau/q-{product}') as response:
            content = await response.text()
        await session.close()

        return content
