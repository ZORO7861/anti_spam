from pyrogram import Client
from sample_config import *
from spr.core.keyboard import *

spr = Client(
    "spr",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="spr/modules"),
)
