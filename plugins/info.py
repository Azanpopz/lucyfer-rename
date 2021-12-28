import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




@Client.on_message(filters.private & filters.command("details"))
async def details(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**🙋🏻‍♂️ First Name :** {update.from_user.first_name}

**🧖‍♂️ Your Second Name :** {last_name}

**🧑🏻‍🎓 Your Username :** {update.from_user.username}

**🆔 Your Telegram ID :** {update.from_user.id}

**🔗 Your Profile Link :** {update.from_user.mention}
""" 
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Client.on_message(filters.private & filters.command("myid"))
async def myid(bot, update):
    text = f"""
**Your Telegram ID :** {update.from_user.id}
"""
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
