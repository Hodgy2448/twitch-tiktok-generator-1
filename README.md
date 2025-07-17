



ː colon



DO THIS!!!
f:
cd twitch-
pipenv shell

python gen.py generate https://www.twitch.tv/thaqil/clip/ImpartialAnimatedClipzNomNom-JnLk34HYv3sNGbVC --output tiktokclip --text "THIS GUY IS SO BAD"






python gen.py generate https://www.youtube.com/watch?v=evCtTIhbDjA --text1 "Liminal Exit - Official Reveal Trailer" --text2 "NEW immersive puzzle simulation game" --cookies cookies.txt --no_facecam



New immersive puzzle simulation game! Wishlist now

Step into an uncanny building trapped in endless loops. Use the elevator, uncover unsettling anomalies, and evade the Entity lurking behind you. Liminal Exit, an immersive walking simulator inspired by liminal spaces. Can you escape, or will you remain forever trapped?

Developer: LittleRedDread
Release Date: Q3 2025 to PC (Steam)


















# Twitch Clip to TikTok Generator

This will locally convert a Twitch clip (or any clip) at a given URL to a vertical format video with facecam that can be uploaded to TikTok, Snapchat, Instagram, or any other vertical format video sharing sites. This tool is aimed at gaming videos.

## Requirements

* Python >= 3.10
* Pipenv
* FFMPEG

## Setup

```sh
git clone https://github.com/chand1012/twitch-tiktok-generator
cd twitch-tiktok-generator
pipenv install
```

## Usage

```sh
pipenv shell
# no extension for output. Will always be MP4
python3 gen.py generate https://clips.twitch.tv/TenaciousPiliableMonitorOhMyDog-G7OYAcQB0bbADKOn --output tiktokclip 
# or if there's no facecam / you don't want facecam
python3 gen.py generate https://clips.twitch.tv/TenaciousPiliableMonitorOhMyDog-G7OYAcQB0bbADKOn --output tiktokclip --no_facecam
# to adjust output resolution (default is 720x1280)
python3 gen.py generate https://clips.twitch.tv/TenaciousPiliableMonitorOhMyDog-G7OYAcQB0bbADKOn --output tiktokclip --width 1080 --height 1920
```

And that's it! Output file will be found in the current working directory.

