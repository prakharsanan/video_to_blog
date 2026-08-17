from pathlib import Path
import yt_dlp

VIDEO_DIR = Path("storage/videos")
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


class YoutubeService:

    @staticmethod
    def download(url: str):

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(VIDEO_DIR / "%(id)s.%(ext)s"),
            "noplaylist": True,
            "quiet": False,

            "extractor_args": {
                "youtube": {
                    "player_client": ["tv_embedded"]
                }
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            file_path = Path(
                ydl.prepare_filename(info)
            )

            # yt-dlp may return a .webm/.mkv path
            # even though the final merged file is MP4
            if file_path.suffix != ".mp4":

                mp4_path = file_path.with_suffix(".mp4")

                if mp4_path.exists():
                    file_path = mp4_path

        return {
            "id": info["id"],
            "title": info["title"],
            "path": str(file_path.resolve())
        }