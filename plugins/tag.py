import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User


API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')



@Client.on_message(filters.forwarded & filters.channel)
async def channeltag(bot, message):
   try:
       chat_id = message.chat.id
       forward_msg = await message.copy(chat_id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")
    
