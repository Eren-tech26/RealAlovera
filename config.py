import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("21968859"))
API_HASH = getenv("21a59d21687f01d448530ee88a26b1eb")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7831283689:AAEhx01EMDE-bfd7vq_amVlBzfghB3LT7lQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://lollolopp0900:slayersan@cluster0.mge1ngz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("-1002485775078", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("6356050482", None))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Rocky9852/anjali_private",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHAT", "https://t.me/VERON_BOTS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/VERON_SUPPORTS")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://files.catbox.moe/jyeumn.jpg")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("BQG2k-wAJD_h-LwRValEU3jXov9nVP6d21ErM8JfFUlzG52of0jVyL-VeO_vx3ChcyPR0ZPs9xFt9tc946gLxvVtu6ak1tG0rNadRe2cl1MK1rfTjarIFLK3DhLGNZ0U4xWbbX8C55Azw9g_qWf-8nScr2cATMxqxpzmJ1YbvdQ5PYMGM9fGsxEabpLIIsnqOZm8Xofeck9iAIDIDCMOnq4YYbiQD5x2llJJioOfAxvxfyTORNlIm9NeQaFObHuJyo3W-b39XfhkYEesxRSxpFg9Bz8lD-uFVaeLYsH6j85nSQe9co8D3V8xbTPlaKWgXH5_A610uMkjrS1eMviS5Oh37Qt65AAAAAFfDNHUAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
STATS_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
STREAM_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/hJTjT5Sx/photo-2025-05-29-07-49-17-7509783130606141452.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

