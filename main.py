from datetime import *
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import Mapped,mapped_column
from base import engine,meta_data,Base,session
from config import *
from handler import *


async def main() -> None:

    bot = Bot(token)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)    

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex_:
        print("Error polling -> ", ex_)
    

if __name__ == "__main__":
    asyncio.run(main())