import asyncio
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


import pyrogram


@pyrogram.Client.on_message(pyrogram.Filters.regex(pattern=".*http.*"))
async def forward(bot, message):
    try:
        await message.forward(
            chat_id=Config.CHANNEL_ID,
            as_copy=True
        )
        await message.reply_text(
            text="<code>Forwaded Sucessfully</code>",
            parse_mode='html',
            quote=True
        )
    except:
        await message.reply_text(
            text="<code>Make Sure That I am Admin in Your Channel or Provided Channel ID is Correct.</code>",
            parse_mode='html',
            quote=True
        )
