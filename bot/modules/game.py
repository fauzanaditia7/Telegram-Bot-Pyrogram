from bot import app, LOGGER
from pyrogram import filters, Client
from datetime import datetime
import random

data = ["JERAPAH", "KUCING", "HARIMAU"]

@app.on_message(filters.command(['game']))
async def game(client, message):
    return await message.reply(random.choice(data), quote=1)

@app.on_message(filters.command(['ping']))
async def ping(client, message):
    start = datetime.now()
    mes = await message.reply("🏓 Pong!!!", quote=True)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    return await mes.edit("🏓 Pong!!!\n⏳ `%sms`" % (duration))

@app.on_message(filters.command(['myinfo']))
async def myinfo(client, message):
    user = await client.get_users(message.from_user.id)
    text = f"""
🆔 {user.id or 0}
👤Username: {user.username or ""}
"""
    
    LOGGER.info(user)
    return await message.reply(text, quote=1)