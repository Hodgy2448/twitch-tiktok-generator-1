import os
from gtts import gTTS  # type: ignore
import requests # type: ignore

TTS_PROVIDER = os.getenv("TTS_PROVIDER", "gtts")  # Change to 'elevenlabs'/'gtts' if desired
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # Set in .env or environment
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "IRHApOXLvnW57QJPQH2P")  # Change to your preferred voice

def generate_voiceover(text: str, output_path: str = "voice.mp3") -> str:
    if not text:
        raise ValueError("No text provided for TTS.")

    if TTS_PROVIDER.lower() == "elevenlabs":
        if not ELEVENLABS_API_KEY:
            raise EnvironmentError("ELEVENLABS_API_KEY is not set.")

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"ElevenLabs API error: {response.text}")

        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ ElevenLabs voiceover saved to {output_path}")
        return output_path

    else:
        tts = gTTS(text=text, lang="en")
        tts.save(output_path)
        print(f"✅ gTTS voiceover saved to {output_path}")
        return output_path
