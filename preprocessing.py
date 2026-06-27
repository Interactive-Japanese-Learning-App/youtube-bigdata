import pandas as pd
from datetime import datetime


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