from pathlib import Path
import subprocess

IMAGE_DIR = Path("storage/images")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)


class ImageService:

    @staticmethod
    def extract(video_path: str, interval: int = 10):

        video_path = Path(video_path)

        output_folder = IMAGE_DIR / video_path.stem
        output_folder.mkdir(parents=True, exist_ok=True)

        output_pattern = output_folder / "frame_%03d.jpg"

        command = [
            "ffmpeg",
            "-i",
            str(video_path),
            "-vf",
            f"fps=1/{interval}",
            str(output_pattern)
        ]

        subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        images = sorted(output_folder.glob("*.jpg"))

        return {
            "directory": str(output_folder.resolve()),
            "images" : [
                f"/storage/images/{video_path.stem}/{img.name}"
                for img in images
            ]
        }