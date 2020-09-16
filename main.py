from asyncio import get_event_loop

from .src.html_handler import html_processing


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(html_processing())
