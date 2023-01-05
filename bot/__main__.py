from bot import OWNER_ID, LOGGER, app
from bot.helper import HELPABLE, MOD_NOLOAD
from bot.modules import ALL_MODULES
from pyrogram import idle, filters
import asyncio
import importlib

loop = asyncio.get_event_loop()

@app.on_message(filters.command("hello"))
async def hello(c, m):
    await c.get_me()
    await m.reply("AAAAAAAAAA", quote=1)

async def start():
    for module in ALL_MODULES:
        imported_module = importlib.import_module("bot.modules." + module)
        if (hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__):
            if imported_module.__MODULE__.lower() in MOD_NOLOAD:
                continue
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (hasattr(imported_module, "__HELP__") and imported_module.__HELP__):
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module

    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1  
    LOGGER.info("Yay your bot is working.!!!")
    LOGGER.info("=" * 65)
    # await app.send_message(OWNER_ID, "HELLLO")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(start())