

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "add_api_id"))
API_HASH = os.environ.get("API_HASH", "add_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "add_bot_token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("your_owner_id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "add_mongdb_name")
DATABASE_URL = os.getenv("DATABASE_URL", "add_mongdb_url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "your_owner_id")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(your_owner_id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "add_private_channel_id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "add_your_channel_id") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'add_your_image_url') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
