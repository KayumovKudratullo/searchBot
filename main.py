import asyncio
from aiogram import Bot, Dispatcher

from database import async_main
from config import TOKEN

async def main():
    await async_main()
    bot = Bot(token='')