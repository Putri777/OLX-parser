from asyncio import run

from .browser import Browser
from .html_handler import HtmlHandler
from .page_parser import PageParser
from .request import Request


async def async_main() -> None:
    """
    When executing the function, it takes the entire method from src and sends it to `runner.py`
    :return: None
    """
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    request = Request(user_agent=user_agent)
    html_handler = HtmlHandler(request)
    page_parser = PageParser(request)
    browser = Browser()

    # print(await html_handler.html_processing())
    # print(await page_parser.page_parse())
    await browser.get_html(await html_handler.html_processing())



def main() -> None:
    """
    Get async function from async_main() and run here
    :return:
    """
    run(async_main())
