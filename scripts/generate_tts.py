import os, re, frontmatter
from google.cloud import texttospeech

# Setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud-key.json"
client = texttospeech.TextToSpeechClient()

def strip_md(md):
    return re.sub(r'[^\S\r\n]+', ' ', re.sub(r'<[^>]+>', '', re.sub(r'\!\[.*?\]\(.*?\)', '', md)))

POSTS_DIR = '_posts'
AUDIO_DIR = 'assets/audio'
os.makedirs(AUDIO_DIR, exist_ok=True)

for file in os.listdir(POSTS_DIR):
    if not file.endswith('.md'): continue
    post = frontmatter.load(os.path.join(POSTS_DIR, file))
    slug = post.get('slug') or re.sub(r'[^\w-]', '', post['title'].lower().replace(' ', '-'))
    audio_path = os.path.join(AUDIO_DIR, f"{slug}.mp3")
    if os.path.exists(audio_path): continue

    text = strip_md(post.content)[:5000]  # TTS limit per request
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    with open(audio_path, 'wb') as out:
        out.write(response.audio_content)
        print(f"✅ Generated: {audio_path}")
