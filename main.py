from asyncio import get_event_loop

from .src import html_handler


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(html_handler.html_processing())
