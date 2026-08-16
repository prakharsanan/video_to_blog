import os
from pathlib import Path

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

TRANSCRIPT_DIR = Path("storage/transcripts")
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)


class WhisperService:

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    @staticmethod
    def transcribe(audio_path: str):

        audio_path = Path(audio_path)

        with open(audio_path, "rb") as file:

            transcription = WhisperService.client.audio.transcriptions.create(
                file=(audio_path.name, file.read()),
                model="whisper-large-v3-turbo",
                response_format="json"
            )

        transcript = transcription.text.strip()

        transcript_path = (
            TRANSCRIPT_DIR /
            f"{audio_path.stem}.txt"
        )

        transcript_path.write_text(
            transcript,
            encoding="utf-8"
        )

        return {
            "text": transcript,
            "path": str(transcript_path.resolve())
        }