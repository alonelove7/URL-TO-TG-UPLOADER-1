import asyncio
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


import pyrogram
from pyrogram import Client, Filters


@pyrogram.Client.on_message(Filters.private & Filters.text)
async def forward(bot, message):
    try:
        await message.forward(
            chat_id=Config.CHANNEL_ID,
            as_copy=True
        )
