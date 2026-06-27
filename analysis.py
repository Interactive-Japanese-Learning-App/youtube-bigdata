import pandas as pd


def analyze(df):
    # Jika data kosong
    if df.empty:
        print("Data kosong!")
        return pd.DataFrame(), pd.DataFrame()

    # Hitung skor trending
    df["score"] = (
        (df["views"] * 0.6) +
        (df["likes"] * 0.3) +
        (df["comments"] * 0.1)
    )

    # Urutkan video berdasarkan skor tertinggi
    trending_df = df.sort_values(
        by="score",
        ascending=False
    ).reset_index(drop=True)

    # Analisis channel
    channel_df = df.groupby("channel").agg({
        "views": "sum",
        "likes": "sum",
        "comments": "sum"
    }).reset_index()

    # Hitung skor channel
    channel_df["score"] = (
        (channel_df["views"] * 0.6) +
        (channel_df["likes"] * 0.3) +
        (channel_df["comments"] * 0.1)
    )

    # Urutkan channel berdasarkan skor
    channel_df = channel_df.sort_values(
        by="score",
        ascending=False
    ).reset_index(drop=True)

    print("\nTOP 10 TRENDING VIDEO")
    print(
        trending_df[
            [
                "title",
                "channel",
                "views",
                "likes",
                "comments",
                "score"
            ]
        ].head(10)
    )

    print("\nTOP 10 CHANNEL")
    print(channel_df.head(10))

    return trending_df, channel_df