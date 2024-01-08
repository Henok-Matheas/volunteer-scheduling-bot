import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.utils.markdown import hbold

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")


create_single_post_router = Router()
class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Choose Group type
aait = KeyboardButton(text="AAIT")
aastu = KeyboardButton(text="AASTU")
remote = KeyboardButton(text="Remote")
ghana = KeyboardButton(text="Ghana")
astu = KeyboardButton(text="ASTU")
all = KeyboardButton(text="All")
custom = KeyboardButton(text="Custom")
cancel = KeyboardButton(text="Cancel")

choose_group_markup = ReplyKeyboardMarkup(keyboard=[[aait, aastu, remote],
                                                    [ghana, astu, custom],
                                                    [all, cancel]], resize_keyboard=True, one_time_keyboard=True)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message(Command("custom"))
async def command_custom_handler(message: Message) -> None:
    """
    This handler receives messages with `/custom` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}! This is custom command")

@dp.message(Command("create_single_post"))
async def command_create_single_post_handler(message: Message) -> None:
    """
    This handler receives messages with `/create_single_post` command and is used to create a single text without scheduling or repititon.
    """
    logging.info("create_single_post command received")
    await message.answer(f"Which groups do you want to send the message to?", reply_markup=choose_group_markup)


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
    # And the run events dispatching
    await dp.start_polling(bot, polling_timeout=2)
    logging.info("Starting Polling...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


