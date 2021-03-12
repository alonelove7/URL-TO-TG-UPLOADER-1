import time
import pyrogram
from pyrogram import Client, filters

@pyrogram.Client.on_message(pyrogram.filters.command(["ping", "ping@xploaderzxbot"]))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
