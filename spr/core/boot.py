from sqlite3 import connect
from spr.utils.db import DB_NAME

# Database connection (safe in sync)
conn = connect(DB_NAME)

# ClientSession aur ARQ ko yaha se hata diya gaya hai
# Sab ARQ-related cheeze ab 'check_nsfw()', 'check_spam()', etc. wrappers me handle hongi

# NOTE: Use 'get_session()' from 'session_utils.py' wherever needed in async context
