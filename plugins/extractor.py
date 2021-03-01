import os
import pyrogram

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import Script
from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@trojanz.on_message(filters.private & (filters.document | filters.video))
async def confirm_dwnld(client, message):
    media = message
    filetype = media.document or media.video

    if filetype.mime_type.startswith("video/"):
        await message.reply_text(
            "**Select the Optins Below**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="DOWNLOAD", callback_data="download_file")],
                [InlineKeyboardButton(text="CANCEL", callback_data="close")]]
            )
        )
    else:
        await message.reply_text(
            "```Invalid Media```",
            quote=True
        )
