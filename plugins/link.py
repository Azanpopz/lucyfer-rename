from os import environ
import aiohttp
from pyrogram import Client, filters
from info import API_ID, API_HASH, API_KEY, BOT_TOKEN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')





@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Open Link", url=f"({short_link})', quote=True"), 
                    InlineKeyboardButton(text="Share Link", url=f"telegram")
                ],
                [InlineKeyboardButton(text="⚙ Join Updates Channel ⚙", url="({short_link})',")]
            ]
        )
    )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://gplinks.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]



