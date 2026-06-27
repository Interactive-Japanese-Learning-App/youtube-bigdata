from pymongo import MongoClient
from config import (
    MONGO_URI,
    DATABASE_NAME,
    VIDEO_COLLECTION,
    CHANNEL_COLLECTION,
    TOP_CHANNEL_COLLECTION
)

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

video_collection = db[VIDEO_COLLECTION]
channel_collection = db[CHANNEL_COLLECTION]
top_channel_collection = db[TOP_CHANNEL_COLLECTION]


def save_video(df):
    if df.empty:
        print("Tidak ada data video untuk disimpan.")
        return

    top_videos = df.head(10)

    for _, row in top_videos.iterrows():

        data = row.to_dict()

        video_collection.replace_one(
            {"video_id": data["video_id"]},
            data,
            upsert=True
        )

    print(f"{len(top_videos)} video berhasil disimpan.")


def save_channel(df):
    if df.empty:
        print("Tidak ada data channel untuk disimpan.")
        return

    top_channels = df.head(10)

    for _, row in top_channels.iterrows():

        data = row.to_dict()

        channel_collection.replace_one(
            {"channel": data["channel"]},
            data,
            upsert=True
        )

    print(f"{len(top_channels)} channel berhasil disimpan.")


def save_top_channel(df):
    if df.empty:
        print("Tidak ada data top channel untuk disimpan.")
        return

    top_channels = df.head(10)

    for _, row in top_channels.iterrows():

        data = row.to_dict()

        top_channel_collection.replace_one(
            {"channel_id": data["channel_id"]},
            data,
            upsert=True
        )

    print(f"{len(top_channels)} top channel berhasil disimpan.")