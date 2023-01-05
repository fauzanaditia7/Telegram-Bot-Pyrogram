from pyrogram import filters
from bot import app, LOGGER

__MODULE__ = "START"
__HELP__ = "Start Message"

@app.on_message(filters.command('start'))
async def start(client, message):
    user = message.from_user
    LOGGER.info("User > ", user)
    return await message.reply("Hello There", quote=1)

# @app.on_message()
# async def onMessage(client, message):
#     await client.get_me()
#     return await message.reply("AAAAAAAAAAAAA")