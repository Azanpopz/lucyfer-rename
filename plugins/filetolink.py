import telebot
import time
import pyshorteners
import os

from os import environ
import aiohttp
from pyrogram import Client, filters
from info import BOT_TOKEN


BOT_TOKEN = environ.get('BOT_TOKEN')



def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)


@bot.on_message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass
