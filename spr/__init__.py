import os
from pyrogram import Client
from spr.core.keyboard import *

# Heroku environment se credentials load karna
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Pyrogram bot client setup
spr = Client(
    "spr",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="spr/modules"),
)
