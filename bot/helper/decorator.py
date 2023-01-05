from bot import LOGGER
from pyrogram import errors
from pyrogram.types import Message
from functools import wraps
import sys
import traceback

def split_limits(text):
    if len(text) < 2048:
        return [text]

    lines = text.splitlines(True)
    small_msg = ''
    result = []
    for line in lines:
        if len(small_msg) + len(line) < 2048:
            small_msg += line
        else:
            result.append(small_msg)
            small_msg = line
    else:
        result.append(small_msg)

    return result

def catch_error(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                exc_type, value=exc_obj, tb=exc_tb,
            )
            error_feedback = split_limits(
                '<b>ERROR</b> | <code>{}</code> | <code>{}</code>\n\n<code>{}</code>\n\n<code>{}</code>\n'.format(
                    0 if not message.from_user else message.from_user.id,
                    0 if not message.chat else message.chat.id,
                    message.text or message.caption,
                    ''.join(errors),
                ),
            )
            LOGGER.error(errors)
            [await client.send_message(message.chat.id, x) for x in error_feedback]
            raise err
    return capture