import math
import os
import time
import asyncio
import logging
import requests
import uuid
from datetime import datetime
from pytz import timezone
from pyrogram import Client, filters, enums, StopPropagation
from pyrogram.errors import MessageNotModified, FloodWait, UserNotParticipant
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent)
from youtube_dl import DownloadError
import youtube_dl
from pornhub_api import PornhubApi
from pornhub_api.backends.aiohttp import AioHttpBackend

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Constants
BOT_USERNAME = "AnimeZenith"

@Client.on_message(filters.command("rip"))
async def handle_single_download(bot: Client, update: Message):
    if len(update.command) < 2:
        await update.reply("Please provide a valid HTTP link.")
        return
    
    http_link = update.command[1]
    await ytdl_downloads(bot, update, http_link)

def get_thumbnail_url(video_url):
    ydl_opts = {'format': 'best', 'quiet': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        try:
            thumbnail_url = info_dict['entries'][0]['thumbnails'][0]['url']
            return thumbnail_url
        except Exception:
            return None

def get_porn_thumbnail_url(video_url):
    ydl_opts = {'format': 'best', 'quiet': True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        try:
            thumbnail_url = info_dict['thumbnail']
            return thumbnail_url
        except Exception as e:
            print(e)
            return None

async def ytdl_downloads(bot: Client, update: filters.Message, http_link: str):
    msg = await update.reply(f"**Link:** {http_link}\n\nDownloading... Please have patience\nLoading...", disable_web_page_preview=True)

    # Determine thumbnail URL based on the link
    if http_link.startswith("https://www.pornhub"):
        thumbnail = get_porn_thumbnail_url(http_link)
    else:
        thumbnail = get_thumbnail_url(http_link)

    ytdl_opts = {
        'format': 'best',
    }
    loop = asyncio.get_event_loop()
    try:
        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            await loop.run_in_executor(None, ydl.download, [http_link])
    except DownloadError:
        await msg.edit("Sorry, there was a problem with that particular video.")
        return

    await msg.edit("⚠️ Please wait...\n\n**Trying to upload...**")
    unique_id = uuid.uuid4().hex

    if thumbnail:
        thumbnail_filename = f"thumbnail_{unique_id}.jpg"
        response = requests.get(thumbnail)
        if response.status_code == 200:
            with open(thumbnail_filename, 'wb') as f:
                f.write(response.content)

    for file in os.listdir('.'):
        if file.endswith(".mp4") or file.endswith('.mkv'):
            try:
                if thumbnail:
                    await bot.send_video(chat_id=update.from_user.id, video=file, thumb=thumbnail_filename,
                                         caption=f"**📁 File Name:** `{file}`\n\nHere is your requested video 🔥\n\nPowered by - @{bot.username}")
                    os.remove(thumbnail_filename)
                else:
                    await bot.send_video(chat_id=update.from_user.id, video=file,
                                         caption=f"**📁 File Name:** `{file}`\n\nHere is your requested video 🔥\n\nPowered by - @{bot.username}")
                os.remove(file)
                break
            except Exception as e:
                await msg.edit(str(e))
                break

    await msg.delete()

@Client.on_inline_query()
async def search(client, inline_query: InlineQuery):
    query = inline_query.query
    backend = AioHttpBackend()
    api = PornhubApi(backend=backend)
    results = []
    try:
        src = await api.search.search(query, ordering="mostviewed")
    except ValueError as e:
        results.append(InlineQueryResultArticle(
            title="No Such Videos Found!",
            description="Sorry! No Such Videos Were Found. Please Try Again",
            input_message_content=InputTextMessageContent(
                message_text="No Such Videos Found!"
            )
        ))
        await inline_query.answer(results,
                                  switch_pm_text="Search Results",
                                  switch_pm_parameter="start")

        return

    videos = src.videos
    await backend.close()

    for vid in videos:
        msg = f"{vid.url}"

        results.append(InlineQueryResultArticle(
            title=vid.title,
            input_message_content=InputTextMessageContent(
                message_text=msg,
            ),
            description=f"Duration : {vid.duration}\nViews : {vid.views}\nRating : {vid.rating}",
            thumb_url=vid.thumb,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Watch online", url=vid.url),
            ]]),
        ))

    await inline_query.answer(results,
                              switch_pm_text="Search Results",
                              switch_pm_parameter="start")
