import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from plugins.helper_functions.cust_p_filters import sudo_filter
from plugins.helper_functions.get_file_id import get_file_id
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"

@Client.on_message(
    filters.command("telegraph") 
)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("Reply to a supported media file")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.message_id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply_text(
            text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>Join :-</b> @FayasNoushad",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="⚙ Join Updates Channel ⚙", url="https://telegram.me/Nasrani_updates")]
            ]
        )
    )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )
