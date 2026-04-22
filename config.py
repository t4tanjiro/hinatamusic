import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# 🔑 Telegram API
API_ID = int(getenv("API_ID", 20574660))
API_HASH = getenv("API_HASH", "6e21188e487b96af1ff5429dedada8ff")

# 🤖 Bot Token
BOT_TOKEN = getenv("BOT_TOKEN", "8392700955:AAHnFaLUPxB1WY1NH109hRYh8lLwjWgKy2M")

# 🍃 MongoDB
MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://rahul:rahulkr@cluster0.szdpcp6.mongodb.net/?retryWrites=true&w=majority"
)

# ⏱ Duration
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# 📜 Logs
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002317259468))

# 👑 Owner
OWNER_ID = int(getenv("OWNER_ID", 7958077163))

# 🔥 Sudo Users
SUDOERS = list(map(int, getenv("SUDOERS", "7958077163 7091230649").split()))

# 🌐 Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# 🎵 APIs
API_URL = getenv("API_URL", "https://api.nexgenbots.xyz")
VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")
API_KEY = getenv("API_KEY", "30DxNexGenBotsbf4759")

# 🔄 Repo Updater
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/t4tanjiro/hinatamusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# 📢 Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbotz_update")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/TBOT_CHATS")

# 🤖 Assistant Auto Leave (FIXED)
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True") == "True"

# 🔐 Privacy
PRIVACY_LINK = getenv(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14"
)

# 🎧 Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# 📂 Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# 📦 File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

# 👤 Assistant Sessions
STRING1 = getenv("STRING_SESSION", "BQE58cQAYQj5XYqYsdsndE8Mnrzz8wEkTNOZKyBWkTiwpnPeY_Awvr4QvAMkSdIExsaj6x1GOA-9A93RlXHVDhsRgRShGqwnFkX6P_XIllw5oUabFuupzvVmL3lbQFCDlpQOCk4UThd8twGM0rfKzllCno3ZBBowsN1ZHREBZXtBFVUy5K5urlNRNQRss8MN123FFLyD409Za6YlmAJ_bYa_CeMWuz98cEqHSLWh2r9eDoyTBctN6O0RxFhcFWEFUrOQ2mTPmfQqxsePFRGODT-KA1_ZpFKJSCZVZnwoFtNjz7BVa96thb2gu576E2Oo5t2uNbsIDMa2V1dXdYWVkEoNfAFIJAAAAABZAnQ-AA")

STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# 🚫 Banned users
BANNED_USERS = filters.user()

# ⚙️ Runtime Data
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# 🖼 Images
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"

# ⏱ Convert duration
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ✅ URL validation
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("Invalid SUPPORT_CHANNEL URL")

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit("Invalid SUPPORT_GROUP URL")
