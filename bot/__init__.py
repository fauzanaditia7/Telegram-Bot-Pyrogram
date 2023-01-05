from pyrogram import Client
from threading import Lock
from config import cfg
import os, time, logging

if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

def getEnv(name: str, key=None):
    if key:
        return os.getenv(name, key)
    return os.getenv(name)
        
logging.basicConfig(
    format='[%(levelname)s] - [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)


OWNER_ID = cfg.OWNER_ID
OPENAI_API_KEY = cfg.OPENAI_API_KEY

app = Client(
    "BOT", api_id=cfg.API_ID, api_hash=cfg.API_HASH, bot_token=cfg.BOT_TOKEN,
    plugins={"root": "bot/modules"}
)
start_time = time.time()
app.start()
lock = Lock()