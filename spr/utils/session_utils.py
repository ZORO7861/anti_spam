# spr/utils/session_utils.py

from aiohttp import ClientSession

session = None

async def get_session():
    global session
    if session is None or session.closed:
        session = ClientSession()
    return session
