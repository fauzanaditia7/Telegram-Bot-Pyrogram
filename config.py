import os
from dotenv import load_dotenv

load_dotenv() #  Meload file config .env

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH")
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



cfg = Config()