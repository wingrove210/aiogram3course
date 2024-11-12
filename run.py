import asyncio
from aiogram import Bot, Dispatcher, F
from config import TOKEN
import logging
from app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
       asyncio.run(main())
    except:
        KeyboardInterrupt('Exit')