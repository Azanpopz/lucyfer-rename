import os
import re
import requests
import traceback
from asyncio import get_running_loop
from io import BytesIO
from .list import list
from database.gtrans_mdb import find_one


from googletrans import Translator
from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message



def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".ogg"
    tts.write_to_fp(audio)
    return audio


@Client.on_message(filters.command(["tts"]))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("💡 Reply to some texts !")
    if not message.reply_to_message.text:
        return await message.reply_text("💡 Reply to some texts !")
    m = await message.reply_text("Processing...😌")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)

@Client.on_message(filters.command(["tr"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tr")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			hehek = InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "language codes", url="https://cloud.google.com/translate/docs/languages"
                                        )
                                    ],
				    [
                                        InlineKeyboardButton(
                                            "✗ close the translate ✗", callback_data="close_data"
                                        )
                                    ],
                                ]
                            )
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```", reply_markup=hehek, quote=True)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 await ms.delete()
				
async def spaste(content: str):
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        resp = requests.post(siteurl, data={"content": content, "extension": "py"})
        response = resp.json()
        link = f"https://spaceb.in/{response['payload']['id']}"
        rawlink = f"{siteurl}{response['payload']['id']}/raw"
        return link, rawlink
    except Exception as e:
        print(e)
        return None


@Client.on_message(filters.command("paste") & ~filters.edited)
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply("Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await message.reply("Only text and documents are supported.")

    m = await message.reply("Pasting...")

    if r.text:
        content = r.text
    elif r.document:
        p_file = await r.download()
        content = open(p_file, "r").read()
        os.remove(p_file)

    link, rawlink = await paste(content)
    s_link, s_rawlink = await spaste(content)
    kb = InlineKeyboardMarkup([[InlineKeyboardButton("PasteBin", url=link), InlineKeyboardButton("SpaceBin", url=s_link)]])
    await message.reply_text(
        f"**Pasted!**\nPasteBin: [Here]({rawlink})\nSpaceBin: [Here]({s_rawlink})",
        quote=True,
        reply_markup=kb,
    )
    await m.delete()
