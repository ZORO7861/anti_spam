import asyncio
from aiohttp import ClientSession
from pyrogram import Client
from sqlite3 import connect

from spr.utils.db import *
from spr.utils.misc import *
from spr.utils.functions import *
from spr.modules import *
from spr.core.keyboard import *
from sample_config import *
from spr.utils.functions import ARQ, ARQ_API_URL, ARQ_API_KEY
from spr.utils.db import DB_NAME

async def create_arq():
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)
    return arq, session

arq, session = asyncio.run(create_arq())

conn = connect(DB_NAME)

spr = Client(
    "spr",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="spr/modules"),
)
