import re
import io
import os
import glob
import frontmatter
from pydub import AudioSegment
from google.cloud import texttospeech

# Constants
POSTS_DIR = "_posts"
OUTPUT_DIR = "assets/audio"
MAX_BYTES = 5000

client = texttospeech.TextToSpeechClient()
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_main_content_only(content):
    try:
        start_match = re.search(r"(?i)^US Citizens Held.*", content, re.MULTILINE)
        start = start_match.start() if start_match else 0
        end_match = re.search(r"(?i)^##\s*Sources", content[start:], re.MULTILINE)
        end = start + end_match.start() if end_match else len(content)
        return content[start:end].strip()
    except Exception:
        return content.strip()

def chunk_text(text, max_bytes):
    paragraphs = text.split("\n")
    chunks = []
    chunk = ""

    for para in paragraphs:
        tentative = (chunk + "\n" + para).strip()
        if len(tentative.encode("utf-8")) > max_bytes:
            if chunk:
                chunks.append(chunk.strip())
            chunk = para
        else:
            chunk = tentative

    if chunk:
        chunks.append(chunk.strip())

    return chunks

def synthesize_speech(text):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    return client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    ).audio_content

def generate_audio(post_path):
    filename = os.path.basename(post_path).replace(".md", "")
    output_path = f"{OUTPUT_DIR}/{filename}.mp3"

    if os.path.exists(output_path):
        print(f"⏩ Skipping (already exists): {filename}")
        return

    print(f"🎤 Generating TTS for: {filename}")
    post = frontmatter.load(post_path)
    content = get_main_content_only(post.content)
    content = re.sub(r"<[^>]+>", "", content)

    chunks = chunk_text(content, MAX_BYTES)
    if not chunks:
        print(f"💥 Error generating audio for {filename}: No valid chunks.")
        return

    combined = AudioSegment.empty()

    try:
        for chunk in chunks:
            audio_bytes = synthesize_speech(chunk)
            segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
            combined += segment
        combined.export(output_path, format="mp3")
        print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"💥 Error generating audio for {filename}: {e}")

for post_path in glob.glob(f"{POSTS_DIR}/**/*.md", recursive=True):
    generate_audio(post_path)
