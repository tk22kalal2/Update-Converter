import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", 21748181))
API_HASH = os.environ.get("API_HASH", 'b1d962414e186e0778911f3183feac33')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6806119336:AAHPgsNAm6muevQanFDVxqKRQ-JFHlsrx5c')
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
OWNER_ID = int(os.environ.get("OWNER_ID", "5651594253"))
DATABASE_NAME = os.environ.get("DATABASE_NAME", "zxlink")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SawanSingh:sawansingh@cluster0.h2prshr.mongodb.net/?retryWrites=true&w=majority")
# Optionnal variables
BROADCAST_AS_COPY = is_enabled((os.environ.get('BROADCAST_AS_COPY', "False")), False)
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/99d583cff0b18c2470c03.jpg')
BIN_CHANNEL = os.environ.get("BIN_CHANNEL", -1001765670990)
#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
BASE_SITE = "zxlink.in"

if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
