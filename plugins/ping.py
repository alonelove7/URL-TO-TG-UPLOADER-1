import os
import time
import pyrogram
from pyrogram import Client, filters

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
Bot = Client(Config.SESSION_NAME, bot_token=Config.TG_BOT_TOKEN, api_id=Config.APP_ID, api_hash=Config.API_HASH)    

@pyrogram.Client.on_message(pyrogram.filters.command(["ping", "ping@xploaderzxbot"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
    
@Bot.on_message(filters.command("bc"))
async def help(bot, cmd):
    await bot.send_message(chat_id=Config.LOG_CHANNEL, text=f"#S")
