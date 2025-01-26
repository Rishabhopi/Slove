from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from UTTAM import app

#--------------------------
MUST_JOIN = ["nenobots", "ll_BOTCHAMBER_ll", "ur_rishu_143"]
#------------------------

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return

    not_joined_channels = []
    main_button = []

    for channel in MUST_JOIN:
        try:
            await app.get_chat_member(channel, msg.from_user.id)
        except UserNotParticipant:
            if channel.isalpha():
                link = "https://t.me/" + channel
            else:
                chat_info = await app.get_chat(channel)
                link = chat_info.invite_link
            not_joined_channels.append(channel)
            main_button.append(
                [InlineKeyboardButton(f"๏Jᴏɪɴ {channel}๏", url=link)]
            )

    if not_joined_channels:
        try:
            await msg.reply_photo(
                photo="https://files.catbox.moe/zfy8qm.jpg",
                caption="๏ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴀʟʟ ʀᴇQᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs, \n\n ᴊᴏɪɴ ᴛʜᴇᴍ ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ!",
                reply_markup=InlineKeyboardMarkup(
                    main_button
                    + [
                        [
                            InlineKeyboardButton("๏Jᴏɪɴ๏", url="https://t.me/ll_BOTCHAMBER_ll"),
                            InlineKeyboardButton("๏Jᴏɪɴ๏", url="https://t.me/ur_rishu_143")
                        ]
                    ]
                )
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass
    else:
        # Proceed with other actions if the user has joined all channels
        pass