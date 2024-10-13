#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler


#Your Telegram Bot Token From Botfather 
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6990928579:AAESLuHis4iPeeekmnxOziZooKj5ffhOrVM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", 3847632))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1a9708f807ddd06b10337f2091c67657")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002074187786"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6907125255"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/d95eed3ec39000ba5f8de.jpg")

#Port
PORT = os.environ.get("PORT", "8030")

DEL_MSG = """⚠️ Attention! ⚠️

🚨 Your file will be automatically deleted in 600 seconds! 🚨

To keep your file, please forward it or download and save to downloads, within the time limit. If the file gets deleted, you can re-download it, and your download progress will be saved just click on the file link again from the channel📥💾

Act now to secure your file! ⏳🔐"""

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Madara:7IlnX3T5C8fkk7ik@cluster0.znu6m5l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

AUTO_DEL = os.environ.get("AUTO_DEL", "True").lower() == "true"
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001968893400"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002031353748"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start pic
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/3ebcefec1b1f0b95f7759.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴀᴋᴋᴀᴀᴀ!! {first}</b>\n\nI can provide files for @ikigai_network\nchannel Members❤️!!\n\nᴊᴜꜱᴛ ᴅᴏɴ'ᴛ ᴏᴠᴇʀʟᴏᴀᴅ ᴍᴇ <a href=https://telegra.ph/file/f602720608f6958927805.jpg>🫣.</a>")
try:
    ADMINS=[6770034949]
    for x in (os.environ.get("ADMINS", "6770034949").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nPlease Join our channel First [ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡] then\n Download by tapping on ⚡️Try Again  \nThank You ❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(2036803347)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
