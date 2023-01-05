from bot import app, LOGGER, OWNER_ID, OPENAI_API_KEY
from bot.helper import catch_error
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import openai
import asyncio

loop = asyncio.get_event_loop()

openai.api_key = OPENAI_API_KEY

async def request(query: str):
    def _ai(q: str):
        return openai.Completion.create(model="text-davinci-003", prompt=query, temperature=0, max_tokens=1000)
    return await loop.run_in_executor(None, _ai, query)

@app.on_message(filters.command('ai'))
async def ai(client, message):
    mes = await message.reply("Checking your input...", quote=1)
    if len(message.command) < 2:
        return await mes.edit("Please parse with argument")
    text = message.text.split(" ", 1)[1]
    response = await request(text)
    text = response['choices'][0]['text']
    LOGGER.info(response)
    await mes.edit(text, parse_mode=ParseMode.HTML)


@app.on_message(filters.command("test"))
async def test(client, message):
    kbd = InlineKeyboardMarkup([[
        InlineKeyboardButton("Click Me", url="https://google.com")
    ]])
    if message.from_user.id != OWNER_ID:
        return await message.reply("MAU NGAPAIN BANG ? ", reply_markup=None, quote=1)
    return await message.reply("HELLO THERE", reply_markup=kbd, quote=1)

@app.on_message(filters.command('a'))
@catch_error
async def aa(client, message):
    int('a')
    await message.reply("A")