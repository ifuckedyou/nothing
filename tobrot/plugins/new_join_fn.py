import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """ <b>Hello 👾 !</b>\n<b>This Is A Telegram Leech Bot 🧲 </b>\n<b>Click Below To Know How To Use Me 📄</b>\n\n<b> Developer 👨🏻‍💻 : @ML_BotUpdates</b>""",
        disable_web_page_preview=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('💫 HOW TO USE 💫', url='https://t.me/MeGLeech/5')
                ],
                [
                    InlineKeyboardButton('⭐ Movie Channel ⭐', url='https://t.me/TamilMoviesML')
                ]
            ]
        ),
    )
