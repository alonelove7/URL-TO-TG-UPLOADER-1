import os
import time
import pyrogram
from pyrogram import Client, filters, errors
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
Bot = Client(Config.SESSION_NAME, bot_token=Config.TG_BOT_TOKEN, api_id=Config.APP_ID, api_hash=Config.API_HASH) 

@Client.on_message(pyrogram.filters.command(["bc"]))
async def help(bot, cmd):
    await bot.send_message(chat_id=Config.LOG_CHANNEL, text=f"#S")
