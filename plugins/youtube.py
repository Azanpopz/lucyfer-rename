from pyrogram import Client ,filters
import os
from py_youtube import Data, Search 
from pyrogram.types import *

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")


    
	


@Client.on_inline_query()
async def search(bot, update):
    
    results = VideosSearch(update.query, limit=50).result()
    answers = []
    
    for result in results:
        title = result["title"]
        views_short = result["viewCount"]["short"]
        duration = result["duration"]
        duration_text = result["accessibility"]["duration"]
        views = result["viewCount"]["text"]
        publishedtime = result["publishedTime"]
        channel_name = result["channel"]["name"]
        channel_link = result["channel"]["link"]
        description = f"{views_short} | {duration}"
        details = f"**Title:** {title}" + "\n" \
        f"**Channel:** [{channel_name}]({channel_link})" + "\n" \
        f"**Duration:** {duration_text}" + "\n" \
        f"**Views:** {views}" + "\n" \
        f"**Published Time:** {publishedtime}" + "\n" \
        "\n" + "**Made by @FayasNoushad**"
        thumbnail = ytthumb.thumbnail(result["id"])
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Watch Video 📹", url=result["link"])]]
        )
        try:
            answers.append(
                InlineQueryResultPhoto(
                    title=title,
                    description=description,
                    caption=details,
                    photo_url=thumbnail,
                    reply_markup=reply_markup
                )
            )
        except:
            pass
    
    await update.answer(answers)
