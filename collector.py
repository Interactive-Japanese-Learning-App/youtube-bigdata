import requests
import pandas as pd
from config import API_KEY

# Video
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

# Channel
def collect_top_channels(max_results=10):
    search_query = (
        "belajar bahasa jepang indonesia"
    )
    url = (
        "https://www.googleapis.com/youtube/v3/search"
    )
    params = {
        "part": "snippet",
        "q": search_query,
        "type": "channel",
        "maxResults": max_results,
        "regionCode": "ID",
        "relevanceLanguage": "id",
        "key": API_KEY
    }

    response = requests.get(
        url,
        params=params
    ).json()
    channels = []
    for item in response.get("items", []):
        channels.append({
            "channel_id":
            item["snippet"]["channelId"],

            "channel_name":
            item["snippet"]["title"],

            "published_at":
            item["snippet"]["publishedAt"]

        })

    channel_df = pd.DataFrame(channels)
    print(
        f"Berhasil mengambil {len(channel_df)} channel"
    )
    return channel_df

def collect_channel_statistics(channel_df):
    url = (
        "https://www.googleapis.com/youtube/v3/channels"
    )
    params = {
        "part": "statistics",
        "id": ",".join(
            channel_df["channel_id"].tolist()
        ),
        "key": API_KEY
    }

    response = requests.get(
        url,
        params=params
    ).json()
    statistics = []
    for item in response.get("items", []):
        statistics.append({
            "channel_id":
            item["id"],
            "subscribers":
            int(
                item["statistics"].get(
                    "subscriberCount",
                    0
                )
            ),
            "total_views":
            int(
                item["statistics"].get(
                    "viewCount",
                    0
                )
            ),
            "total_videos":
            int(
                item["statistics"].get(
                    "videoCount",
                    0
                )
            )
        })

    stats_df = pd.DataFrame(statistics)
    print(
        f"Berhasil mengambil statistik {len(stats_df)} channel"
    )
    return stats_df