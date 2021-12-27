import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')



@Client.on_message(filters.via_bot & filters.group)
async def inline(bot,message):
     await message.delete()
	
