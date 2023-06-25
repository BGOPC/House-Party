from os import getenv
from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = str(getenv("CLIENT_ID"))
CLIENT_SECRET = str(getenv("CLIENT_SECRET"))
REDIRECT_URI = "http://127.0.0.1:8000/spotify/redirect"
