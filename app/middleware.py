from aiogram.types import TelegramObject
from aiogram import BaseMiddleware
from typing import Any, Awaitable, Callable, Dict

class TestMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print('Events Before middleware')
        result = await handler(event, data)
        print('Events after Middleware')
        return result