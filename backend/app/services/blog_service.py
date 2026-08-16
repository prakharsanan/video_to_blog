import os
from pathlib import Path

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

BLOG_DIR = Path("storage/blogs")
BLOG_DIR.mkdir(parents=True, exist_ok=True)


class BlogService:

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    @staticmethod
    def generate(transcript: str, video_id: str, video_title: str):

        prompt = f"""
You are an expert technical content writer and editor.

Your task is to convert the following YouTube video transcript into a well-structured, engaging, and professional blog article.

Video Title:
{video_title}

Transcript:
{transcript}

Instructions:
1. Use the video title as the blog title if it is appropriate; otherwise, create a better SEO-friendly title.
2. Write an engaging introduction (2-3 paragraphs).
3. Organize the content into logical sections using Markdown headings (## and ###).
4. Rewrite the transcript into natural, readable prose instead of preserving conversational speech.
5. Remove filler words, repeated sentences, pauses, and unnecessary speech artifacts.
6. Correct grammar, punctuation, and sentence structure.
7. Preserve all important facts, technical explanations, and examples from the transcript.
8. Do NOT invent or add facts that are not present in the transcript.
9. If the transcript is incomplete or unclear, summarize only the available information without making assumptions.
10. End with a concise conclusion summarizing the key takeaways.
11. Return only valid Markdown. Do not include explanations, notes, or code fences.

The blog should have the following structure:

# Title

Introduction

## Section 1

Content...

## Section 2

Content...

## Section 3

Content...

## Conclusion

Generate the complete blog now.
"""

        completion = BlogService.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
        )

        blog = completion.choices[0].message.content

        blog_path = BLOG_DIR / f"{video_id}.md"

        blog_path.write_text(
            blog,
            encoding="utf-8"
        )

        return {
            "title": blog.split("\n")[0].replace("#", "").strip(),
            "content": blog,
            "path": str(blog_path.resolve())
        }