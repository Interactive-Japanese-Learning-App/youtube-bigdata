import pandas as pd
from datetime import datetime

# Video
def prepare_data(video_df, stats_df):

    # Jika salah satu DataFrame kosong
    if video_df.empty or stats_df.empty:
        print("Data kosong!")
        return pd.DataFrame()

    # Merge berdasarkan video_id
    df = pd.merge(video_df, stats_df, on="video_id", how="inner")

    # Hapus data duplikat
    df = df.drop_duplicates(subset=["video_id"])

    # Handle missing value
    df["views"] = df["views"].fillna(0)
    df["likes"] = df["likes"].fillna(0)
    df["comments"] = df["comments"].fillna(0)

    # Konversi tipe data
    df["views"] = pd.to_numeric(
        df["views"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["likes"] = pd.to_numeric(
        df["likes"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["comments"] = pd.to_numeric(
        df["comments"],
        errors="coerce"
    ).fillna(0).astype(int)

    # Konversi tanggal publish
    df["published_at"] = pd.to_datetime(
        df["published_at"],
        errors="coerce"
    )

    # Tambahkan waktu update
    df["updated_at"] = datetime.now()

    # Reset index
    df = df.reset_index(drop=True)

    print(f"Jumlah data setelah preprocessing: {len(df)}")

    return df

# Channel Berdasarkan Video
def prepare_channel_data(channel_df, stats_df):

    if channel_df.empty or stats_df.empty:
        return pd.DataFrame()

    df = pd.merge(
        channel_df,
        stats_df,
        on="channel_id"
    )

    # hapus duplicate
    df = df.drop_duplicates(
        subset=["channel_id"]
    )

    # handle missing value
    df["subscribers"] = df["subscribers"].fillna(0)
    df["total_views"] = df["total_views"].fillna(0)
    df["total_videos"] = df["total_videos"].fillna(0)

    # convert tipe data
    df["subscribers"] = pd.to_numeric(
        df["subscribers"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["total_views"] = pd.to_numeric(
        df["total_views"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["total_videos"] = pd.to_numeric(
        df["total_videos"],
        errors="coerce"
    ).fillna(0).astype(int)

    # convert tanggal
    df["published_at"] = pd.to_datetime(
        df["published_at"],
        errors="coerce"
    )

    # waktu update
    df["updated_at"] = datetime.now()

    return df.reset_index(drop=True)

# Channel Top Berdasarkan YT
def analyze_top_channels(df):

    if df.empty:
        return df

    df["score"] = (
        df["total_views"] * 0.6 +
        df["subscribers"] * 0.3 +
        df["total_videos"] * 0.1
    )

    top_channels = df.sort_values(
        by="score",
        ascending=False
    )

    return top_channels