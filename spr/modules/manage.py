from os import remove
import aiohttp

from pyrogram import filters
from pyrogram.types import Message

from spr import spr, SUDOERS
from spr.utils.db import (disable_nsfw, disable_spam, enable_nsfw,
                          enable_spam, is_nsfw_enabled,
                          is_spam_enabled)
from spr.utils.misc import admins, get_file_id

__MODULE__ = "Manage"
__HELP__ = """
/anti_nsfw [ENABLE|DISABLE] - Enable or disable NSFW Detection.
/anti_spam [ENABLE|DISABLE] - Enable or disable Spam Detection.

/nsfw_scan - Classify a media.
/spam_scan - Get Spam predictions of replied message.
"""

# Replace with your custom NSFW API
API_URL = "KIAWNM-MBDAEI-FCVDQI-OPLUBA-ARQ"

# NSFW scan function using aiohttp
async def custom_nsfw_scan(file_path):
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as f:
            form = aiohttp.FormData()
            form.add_field("file", f, filename="image.jpg", content_type="application/octet-stream")
            async with session.post(API_URL, data=form) as resp:
                return await resp.json()

@spr.on_message(filters.command("anti_nsfw") & ~filters.private, group=3)
async def nsfw_toggle_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /anti_nsfw [ENABLE|DISABLE]")

    if message.from_user:
        user = message.from_user
        chat_id = message.chat.id
        if user.id not in SUDOERS and user.id not in (await admins(chat_id)):
            return await message.reply_text("You don't have enough permissions")

    status = message.text.split(None, 1)[1].strip().lower()
    chat_id = message.chat.id
    if status == "enable":
        if is_nsfw_enabled(chat_id):
            return await message.reply("Already enabled.")
        enable_nsfw(chat_id)
        await message.reply_text("Enabled NSFW Detection.")
    elif status == "disable":
        if not is_nsfw_enabled(chat_id):
            return await message.reply("Already disabled.")
        disable_nsfw(chat_id)
        await message.reply_text("Disabled NSFW Detection.")
    else:
        await message.reply_text("Unknown Suffix, Use /anti_nsfw [ENABLE|DISABLE]")

@spr.on_message(filters.command("anti_spam") & ~filters.private, group=3)
async def spam_toggle_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /anti_spam [ENABLE|DISABLE]")

    if message.from_user:
        user = message.from_user
        chat_id = message.chat.id
        if user.id not in SUDOERS and user.id not in (await admins(chat_id)):
            return await message.reply_text("You don't have enough permissions")

    status = message.text.split(None, 1)[1].strip().lower()
    chat_id = message.chat.id
    if status == "enable":
        if is_spam_enabled(chat_id):
            return await message.reply("Already enabled.")
        enable_spam(chat_id)
        await message.reply_text("Enabled Spam Detection.")
    elif status == "disable":
        if not is_spam_enabled(chat_id):
            return await message.reply("Already disabled.")
        disable_spam(chat_id)
        await message.reply_text("Disabled Spam Detection.")
    else:
        await message.reply_text("Unknown Suffix, Use /anti_spam [ENABLE|DISABLE]")

@spr.on_message(filters.command("nsfw_scan"), group=3)
async def nsfw_scan_command(_, message: Message):
    err = "Reply to an image/document/sticker/animation to scan it."
    if not message.reply_to_message:
        return await message.reply_text(err)

    reply = message.reply_to_message
    if not any([reply.document, reply.photo, reply.sticker, reply.animation, reply.video]):
        return await message.reply_text(err)

    m = await message.reply_text("Scanning...")
    file_id = get_file_id(reply)
    if not file_id:
        return await m.edit("Something went wrong while getting file ID.")

    file = await spr.download_media(file_id)

    try:
        results = await custom_nsfw_scan(file)
    except Exception as e:
        remove(file)
        return await m.edit(f"API Error: {e}")

    remove(file)

    if not results.get("ok"):
        return await m.edit(results.get("result", "Scan failed."))

    r = results["result"]
    await m.edit(
        f"""
**Neutral:** `{r['neutral']} %`
**Porn:** `{r['porn']} %`
**Hentai:** `{r['hentai']} %`
**Sexy:** `{r['sexy']} %`
**Drawings:** `{r['drawings']} %`
**NSFW:** `{r['is_nsfw']}`
"""
    )

@spr.on_message(filters.command("spam_scan"), group=3)
async def scanNLP(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to scan it.")
    r = message.reply_to_message
    text = r.text or r.caption
    if not text:
        return await message.reply("Can't scan that.")

    # Replace with your own spam analysis API call here if needed
    return await message.reply("ARQ removed. Add your custom spam scan API here.")
