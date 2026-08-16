from pathlib import Path
import subprocess

AUDIO_DIR = Path("storage/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


class AudioService:

    @staticmethod
    def extract(video_path: str):

        video_path = Path(video_path)

        output_path = AUDIO_DIR / f"{video_path.stem}.wav"

        command = [
            "ffmpeg",
            "-y",
            "-i",
            str(video_path),
            "-vn",
            "-acodec",
            "pcm_s16le",
            "-ar",
            "16000",
            "-ac",
            "1",
            str(output_path)
        ]

        subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        return {
            "path": str(output_path.resolve())
        }