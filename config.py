from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","14800186"))
API_HASH = getenv("API_HASH","7b1f5b8e41eaaa29b8f4e5c4aecce7bf")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = ("MONGO_DB_URI","mongodb+srv://shivamyadav:shivam.yadav_23@cluster0.0awjqhr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", https://t.me/BotVerseRavi)
