from aiohttp import ClientSession

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


async def request(product: str) -> str:
    session = ClientSession()
    async with session.get(headers=user_agent, url=f'https://www.olx.kz/kokshetau/q-{product}') as response:
        content = await response.text()
    await session.close()

    return content

