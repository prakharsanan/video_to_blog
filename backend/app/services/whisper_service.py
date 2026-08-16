from pathlib import Path
import whisper

TRANSCRIPT_DIR = Path("storage/transcripts")
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)


class WhisperService:

    model = whisper.load_model("tiny")

    @staticmethod
    def transcribe(audio_path: str):

        result = WhisperService.model.transcribe(audio_path)

        transcript = result["text"].strip()

        transcript_path = (
            TRANSCRIPT_DIR /
            f"{Path(audio_path).stem}.txt"
        )

        transcript_path.write_text(
            transcript,
            encoding="utf-8"
        )

        return {
            "text": transcript,
            "path": str(transcript_path.resolve())
        }