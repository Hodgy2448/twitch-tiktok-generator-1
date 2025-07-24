import os
import re
import requests
import whisper
from gtts import gTTS  # type: ignore
from TTS.api import TTS as CoquiTTS  # type: ignore
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip  # type: ignore
from pydub import AudioSegment  # type: ignore

TTS_PROVIDER = os.getenv("TTS_PROVIDER", "coqui").lower()  # Options: 'elevenlabs', 'gtts', or 'coqui'
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "IRHApOXLvnW57QJPQH2P")


def generate_voiceover(text: str, output_path: str = "voice.mp3") -> str:
    """Generates a voiceover using the selected TTS provider."""
    if not text:
        raise ValueError("No text provided for TTS.")

    if TTS_PROVIDER == "elevenlabs":
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

    elif TTS_PROVIDER == "coqui":
        tts = CoquiTTS(model_name="tts_models/en/vctk/vits")
        speaker = "p226"  # British male voice from VCTK
        tts.tts_to_file(text=text, file_path=output_path, speaker=speaker)
        print(f"✅ Coqui TTS voiceover (p226) saved to {output_path}")
        return output_path

    elif TTS_PROVIDER == "gtts":
        tts = gTTS(text=text, lang="en", tld="co.uk")
        tts.save(output_path)
        print(f"✅ gTTS voiceover saved to {output_path}")
        return output_path

    else:
        raise ValueError(f"Unsupported TTS provider: {TTS_PROVIDER}")


def generate_srt_from_audio(audio_path: str, srt_path: str) -> str:
    """Transcribes audio and saves it as an SRT subtitle file using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    segments = result['segments']

    def format_timestamp(seconds: float) -> str:
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds - int(seconds)) * 1000)
        return f"{h:02}:{m:02}:{s:02},{ms:03}"

    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            start = segment['start']
            end = segment['end']
            text = segment['text'].strip()
            srt_file.write(f"{i}\n")
            srt_file.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            srt_file.write(f"{text}\n\n")

    print(f"✅ Subtitles saved to {srt_path}")
    return srt_path


def parse_srt_to_tuples(srt_path: str, delay_seconds: float = 0.0):
    """Parses SRT subtitles into (start, end, text) tuples with optional delay."""
    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(\d+)\n(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n"
    matches = re.findall(pattern, content, re.DOTALL)

    def to_seconds(ts):
        h, m, s_ms = ts.split(":")
        s, ms = s_ms.split(",")
        return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

    return [
        (
            round(to_seconds(start) + delay_seconds, 3),
            round(to_seconds(end) + delay_seconds, 3),
            text.replace("\n", " ")
        )
        for _, start, end, text in matches
    ]


def generate_voiceover_with_captions(
    text: str,
    audio_path: str = "voice.mp3",
    srt_path: str = "captions.srt",
    delay: float = 8.0
):
    """Generates voiceover audio and corresponding subtitles with delay."""
    audio_file = generate_voiceover(text, audio_path)
    boost_audio_volume(audio_file, audio_file)
    subtitle_file = generate_srt_from_audio(audio_file, srt_path)
    caption_tuples = parse_srt_to_tuples(subtitle_file, delay_seconds=delay)
    return audio_file, caption_tuples


def merge_voiceover_with_video_audio(video_path: str, voice_path: str, output_path: str,delay:float = 8.0):
    """Merges voiceover with video audio, applying volume reduction and delay."""
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not os.path.exists(voice_path):
        raise FileNotFoundError(f"Voice file not found: {voice_path}")

    video = VideoFileClip(video_path)
    clip_audio = video.audio.volumex(0.3)

    try:
        voiceover = AudioFileClip(voice_path)
        delayed_voiceover = voiceover.set_start(delay)
    except Exception as e:
        raise RuntimeError(f"Failed to process voiceover audio: {e}")

    combined_audio = CompositeAudioClip([clip_audio, delayed_voiceover])
    final_video = video.set_audio(combined_audio)

    print(f"🎬 Writing final video to {output_path}...")
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")


def boost_audio_volume(input_path: str, output_path: str, gain_db: float = 6.0):
    """Increases the volume of an audio file by the specified decibel gain."""
    audio = AudioSegment.from_file(input_path)
    louder_audio = audio + gain_db
    louder_audio.export(output_path, format="mp3")
    print(f"🔊 Boosted audio saved to {output_path}")
