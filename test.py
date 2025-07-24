from TTS.api import TTS
from TTS.utils.manage import ModelManager

tts = TTS(model_name="tts_models/en/ek1/tacotron2")

# Specify the speaker ID
speaker_id = "p226"
#speaker_id = "p317"
print("Available TTS models:")
manager = ModelManager()
models = manager.list_models()
for model_name in models:
    print(model_name)

# Generate speech using the chosen speaker
tts.tts_to_file(
    text="Hello! This is a British English male voice.",
    speaker=speaker_id,
    file_path="voice.mp3"
)


