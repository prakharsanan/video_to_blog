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
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = Path(ydl.prepare_filename(info))

            # If the merge created an MP4, adjust the returned path
            if file_path.suffix != ".mp4":
                mp4_path = file_path.with_suffix(".mp4")
                if mp4_path.exists():
                    file_path = mp4_path

        return {
            "id": info["id"],
            "title": info["title"],
            "path": str(file_path.resolve())
        }