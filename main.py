from collector import collect_data, collect_statistics
from preprocessing import prepare_data
from analysis import analyze
from database import save_video, save_channel


def main():
    try:
        print("YOUTUBE BIG DATA PIPELINE")

        print("\n[1] Collecting video data: ")
        video_df = collect_data()
        print(f"Berhasil mengambil {len(video_df)} video")


        print("\n[2] Collecting video statistics:")
        stats_df = collect_statistics(video_df)
        print(f"Berhasil mengambil statistik {len(stats_df)} video")

        print("\n[3] Preparing data:")
        prepared_df = prepare_data(
            video_df,
            stats_df
        )
        print(f"Total data siap dianalisis : {len(prepared_df)}")

        print("\n[4] Analyzing data:")
        trending_df, channel_df = analyze(prepared_df)

        print("\n[5] Saving to MongoDB:")
        save_video(trending_df)
        save_channel(channel_df)
        print("\nPipeline selesai!")

    except Exception as e:
        print("\nTerjadi Error")
        print(e)

if __name__ == "__main__":
    main()