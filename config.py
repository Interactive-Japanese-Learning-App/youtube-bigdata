import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY belum diisi di file .env atau GitHub Secrets.")

if not MONGO_URI:
    raise ValueError("MONGO_URI belum diisi di file .env atau GitHub Secrets.")

DATABASE_NAME = "bigdata_youtube"
VIDEO_COLLECTION = "videos"
CHANNEL_COLLECTION = "channels"
TOP_CHANNEL_COLLECTION = "top_channels"