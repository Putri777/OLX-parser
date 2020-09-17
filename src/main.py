from asyncio import run

from .html_handler import HtmlHandler
from .page_parser import PageParser
from .request import Request


async def async_main():
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    request = Request(user_agent=user_agent)
    html_handler = HtmlHandler(request)
    page_parser = PageParser(request)

    await html_handler.html_processing()
    await page_parser.page_parse()


def main():
    run(async_main())
