from asyncio import run

from .html_handler import html_processing


async def async_main():
    await html_processing()


def main():
    run(async_main())

