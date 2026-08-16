from app.services.youtube_services import YoutubeService
from app.services.audio_service import AudioService
from app.services.whisper_service import WhisperService
from app.services.blog_service import BlogService
from app.services.image_service import ImageService


class PipelineService:

    @staticmethod
    def run(url: str):

        # Download video
        video = YoutubeService.download(url)

        # Extract audio
        audio = AudioService.extract(video["path"])

        # Transcribe audio
        transcript = WhisperService.transcribe(audio["path"])

        # Generate blog
        blog = BlogService.generate(
            transcript["text"],
            video["id"],
            video["title"]
        )

        # Extract images
        images = ImageService.extract(video["path"])

        return {
            "video": video,
            "audio": audio,
            "transcript": transcript,
            "blog": blog,
            "images": images
        }