#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22187182"))
API_HASH = environ.get("API_HASH", "28a7bb842e7bf1f4219248b5a5a51a8b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "5148965221"))
CREDIT = environ.get("CREDIT", "RISHI")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5148965221').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5148965221').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

