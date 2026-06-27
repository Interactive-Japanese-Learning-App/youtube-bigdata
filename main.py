from collector import (
    collect_data,
    collect_statistics,
    collect_top_channels,
    collect_channel_statistics
)

from preprocessing import (
    prepare_data,
    prepare_channel_data
)

from analysis import (
    analyze,
    analyze_top_channels
)

from database import (
    save_video,
    save_channel,
    save_top_channel
)


def main():
    try:
        print("YOUTUBE BIG DATA PIPELINE")
        print("\n[1] Collecting video data:")
        video_df = collect_data()
        print(
            f"Berhasil mengambil {len(video_df)} video"
        )

        print("\n[2] Collecting video statistics:")
        stats_df = collect_statistics(video_df)
        print(
            f"Berhasil mengambil statistik {len(stats_df)} video"
        )

        print("\n[3] Preparing video data:")
        prepared_df = prepare_data(
            video_df,
            stats_df
        )
        print(
            f"Total data siap dianalisis : {len(prepared_df)}"
        )

        print("\n[4] Analyzing video data:")
        trending_df, channel_df = analyze(
            prepared_df
        )

        print("\n[5] Saving video data:")
        save_video(trending_df)
        save_channel(channel_df)

        print("\n[6] Collecting top channel data:")
        yt_channel_df = collect_top_channels()
        print(
            f"Berhasil mengambil {len(yt_channel_df)} channel"
        )

        print("\n[7] Collecting channel statistics:")
        yt_channel_stats = collect_channel_statistics(
            yt_channel_df
        )
        print(
            f"Berhasil mengambil statistik {len(yt_channel_stats)} channel"
        )

        print("\n[8] Preparing channel data:")
        prepared_channel = prepare_channel_data(
            yt_channel_df,
            yt_channel_stats
        )

        print(
            f"Total channel siap dianalisis : {len(prepared_channel)}"
        )

        print("\n[9] Analyzing top channels:")
        top_channel_df = analyze_top_channels(
            prepared_channel
        )

        print("\n[10] Saving top channels:")
        save_top_channel(
            top_channel_df
        )

        print("\nPipeline selesai!")

    except Exception as e:
        print("\nTerjadi Error:")
        print(e)


if __name__ == "__main__":
    main()