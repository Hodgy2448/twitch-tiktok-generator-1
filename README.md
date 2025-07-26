



ː colon

python gen.py generate https://www.twitch.tv/thaqil/clip/ImpartialAnimatedClipzNomNom-JnLk34HYv3sNGbVC --output tiktokclip --text "THIS GUY IS SO BAD"
python gen.py generate https://video.fastly.steamstatic.com/store_trailers/257121821/movie480_vp9.webm?t=1744279759 --text1 "Try To Drive – Official Co-op Gameplay Trailer" --text2 "Tandem cycling, chaos & teamwork" --cookies cookies.txt --no_facecam
python gen.py generate https://www.youtube.com/watch?v=KK30yerMcsA --text1 "Out of Time" --text2 "New Co op Rouglike" --text3 "" --cookies cookies.txt --no_facecam
DO THIS!!!
f:
cd twitch-
pipenv shell





python gen.py generate https://www.youtube.com/watch?v=dLGA0lrdGAs --text1 "Borderlands 4" --text2 "Rafa Gameplay" --text3 "" --cookies cookies.txt --no_facecam

New Borderlands Rafa Gameplay! This is going to be so good

Get ready for war on Kairos. Rafa the Exo‑Soldier delivers close‑quarters slashes, mid‑range cannon fire, and devastating plasma blasts from his Deadframe exo‑suit in this high‑octane gameplay showcase.

Developer: Gearbox Software  
Release Date: September 12, 2025 (PS5, Xbox Series X|S, PC); October 3, 2025 (Nintendo Switch 2)  
Platforms: PlayStation 5, Xbox Series X|S, PC (Steam & Epic Games Store), Nintendo Switch 2













    # Hardcoded text background image
    # text_bg_path = os.path.join(os.path.dirname(__file__), 'background_title_4k.png')
    # input_args += f' -i "{text_bg_path}"'
    # filter_complex += f'; [{last_label}][{input_index}:v] overlay=0:440 [d]'
    # last_label = 'd'
    # input_index += 1

    # text_bg_path2 = os.path.join(os.path.dirname(__file__), 'populargamingcontent_tag_4k.png')
    # input_args += f' -i "{text_bg_path2}"'
    # filter_complex += f'; [{last_label}][{input_index}:v] overlay=700:440 [d]'
    # last_label = 'd'
    # input_index += 1

if overlay_text_bottom:
        wrapped_lines = textwrap.wrap(overlay_text_bottom, width=25)
        for i, line in enumerate(wrapped_lines):
            safe_text = line.replace("'", r"\'") + "\u00A0\u00A0"
            y_pos = f"h-{930 - i * 200}"
            filter_complex += (
                f'; [{last_label}]drawtext='
                f"text='{safe_text} ':" 
                f"fontfile=Bangers-Regular.ttf:"
                f"fontcolor=white:fontsize=180:x=(w-text_w)/2+12:y={y_pos}:"
                f"borderw=8:bordercolor=black"
                f"[b{i}]"
            )
            last_label = f'b{i}'


10 sec video:
https://www.youtube.com/watch?v=lTTajzrSkCw

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

