import time
import asyncio
from datetime import datetime
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["commands", "commands@xploaderzxbot"]))
async def command(client, message):
    await message.reply_text("Here r the Commands \n/upload - Uploads the URL to Telegram as File \n/me - Shows your plan \n/upgrade - Upgrades your existing plan \n/generatecustomthumbnail - Saves the photo as Thumbnail for ur all Files/Videos \n/deletethumbnail - Delete the saved thumbnail \n/help - Shows help Message \n/rename - Renames any file \n/generatescss - Generates screenshots from Video(can be file also) \n/unzip - Unzip and the uploads files \n/downloadmedia - First step for trimming (Saves video for trimming) \n/trim - Trims saved video \n/storageinfo - Shows info of current media saved \n/clearmedia - Clears current media \n/c_2_video - Convert from file 2 video \n \n Now Rock and Roll \n© @v_m_7_0_3 😉 ")
