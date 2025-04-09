from aiohttp import ClientSession
from sqlite3 import connect
from spr.vars import ARQ_API_URL, ARQ_API_KEY
from spr.utils.db import DB_NAME

session = ClientSession()
conn = connect(DB_NAME)

# NSFW Checker
async def check_nsfw(image_url: str):
    async with session.post(f"{ARQ_API_URL}/nsfw", json={
        "image": image_url,
        "key": ARQ_API_KEY
    }) as resp:
        return await resp.json()

# Spam Checker
async def check_spam(text: str):
    async with session.post(f"{ARQ_API_URL}/spam", json={
        "text": text,
        "key": ARQ_API_KEY
    }) as resp:
        return await resp.json()
