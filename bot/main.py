import asyncio
import logging
import sys
import os
from typing import Any, Dict
from aiogram import Bot, Dispatcher, types, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
)
from aiogram.utils.markdown import hbold
from handlers.create_single_post import create_single_post_router

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "../"))
from config import TOKEN


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message(Command("custom"))
async def command_custom_handler(message: Message) -> None:
    """
    This handler receives messages with `/custom` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! This is custom command")

# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         logging.info("Sending message copy...")
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError as err:
#         # But not all the types is supported to be copied so need to handle it
#         logging.error("Cannot send message copy. Type is not supported.",err)
#         await message.answer("Nice try!")

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.info("Starting bot...")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # dp.include_router(create_single_post_router)

    # And the run events dispatching
    await dp.start_polling(bot, polling_timeout=2)

    logging.info("Starting Polling...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


