import os
import time
import pyrogram
from pyrogram import Client, filters

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
Bot = Client(Config.SESSION_NAME, bot_token=Config.TG_BOT_TOKEN, api_id=Config.APP_ID, api_hash=Config.API_HASH) 

@Bot.on_message(filters.command("bc"))
async def help(bot, cmd):
    await bot.send_message(chat_id=Config.LOG_CHANNEL, text=f"#S")
