from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

bot = Bot('5340751975:AAH3zzeam-t7aUK3X4qr1slbNgqp2gDWc7s')
dp = Dispatcher(bot, storage=storage)