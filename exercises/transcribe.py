import os
import requests
from mutagen.mp3 import MP3
from dotenv import load_dotenv

# Load auth token from .env file
load_dotenv()
access_token = os.getenv("AUTH_TOKEN")

# Define language codes
language_codes = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg",
}

# Prompt for audio file path
audio_path = input("Please provide path to the audio file (Audio length less than 5 minutes): ").strip()

# Validate file existence
if not os.path.exists(audio_path):
    print("❌ File not found. Please check the path and try again.")
    exit()

# Validate audio length (in seconds)
try:
    audio = MP3(audio_path)
    duration_sec = audio.info.length
    if duration_sec > 300:
        print("❌ Audio is longer than 5 minutes. Please provide a shorter file.")
        exit()
except Exception as e:
    print(f"❌ Could not process audio: {e}")
    exit()

# Prompt for language
print("Please choose the target language:")
for lang in language_codes:
    print(f"- {lang}")
target_lang = input("Language: ").strip()

if target_lang not in language_codes:
    print("❌ Invalid language. Please choose from the list.")
    exit()

lang_code = language_codes[target_lang]

# API request
url = "https://api.sunbird.ai/tasks/stt"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}",
}

with open(audio_path, "rb") as audio_file:
    files = {
        "audio": (os.path.basename(audio_path), audio_file, "audio/mpeg"),
    }
    data = {
        "language": lang_code,
        "adapter": lang_code,
        "whisper": True,
    }

    print(f"\nTranscribing audio in {target_lang.lower()}...\n")
    response = requests.post(url, headers=headers, files=files, data=data)

# Handle response
if response.status_code == 200:
    result = response.json()
    print(f"✅ Audio transcription text in {target_lang.lower()}:\n{result.get('text', '[No text returned]')}")
else:
    print(f"❌ Transcription failed: {response.status_code} - {response.text}")
