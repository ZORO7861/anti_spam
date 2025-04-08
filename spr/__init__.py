# spr/__init__.py

from pyrogram import Client
from spr.vars import API_ID, API_HASH, BOT_TOKEN
from spr.core.keyboard import *

spr = Client(
    "spr",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="spr/modules"),
)
