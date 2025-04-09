import asyncio
from aiohttp import ClientSession
from sqlite3 import connect
from spr.vers import ARQ, ARQ_API_URL, ARQ_API_KEY
from spr.utils.db import DB_NAME

async def create_arq():
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)
    return arq, session

arq, session = asyncio.run(create_arq())
conn = connect(DB_NAME)
