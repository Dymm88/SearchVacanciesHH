import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
TOKEN = os.getenv('TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
EMAIL = os.getenv('EMAIL')
RESUME = os.getenv('RESUME_ID')

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "User-Agent": f"VacancyBot/1.0 ({EMAIL})",  # VacancyBot название моего приложения, необходимо подставить свое
    "Content-Type": "application/json",
}
