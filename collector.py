import requests
import pandas as pd
from config import API_KEY


def collect_data(max_results=20):
    search_query = (
        "belajar bahasa jepang "
        "hiragana katakana pemula "
        "bahasa indonesia "
        "indo"
    )
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": search_query,
        "type": "video",
        "videoDuration": "medium",
        "order": "viewCount",
        "maxResults": max_results,
        "regionCode": "ID",
        "relevanceLanguage": "id",
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    videos = []
    for item in data.get("items", []):
        if "videoId" not in item["id"]:
            continue
        videos.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"]
        })
    return pd.DataFrame(videos)


def collect_statistics(video_df):
    if video_df.empty:
        return pd.DataFrame()

    video_ids = video_df["video_id"].tolist()
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics",
        "id": ",".join(video_ids),
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    statistics = []

    for item in data.get("items", []):
        statistics.append({
            "video_id": item["id"],
            "views": int(
                item["statistics"].get("viewCount", 0)
            ),
            "likes": int(
                item["statistics"].get("likeCount", 0)
            ),
            "comments": int(
                item["statistics"].get("commentCount", 0)
            )

        })
    return pd.DataFrame(statistics)