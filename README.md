



ː colon

python gen.py generate https://www.twitch.tv/thaqil/clip/ImpartialAnimatedClipzNomNom-JnLk34HYv3sNGbVC --output tiktokclip --text "THIS GUY IS SO BAD"
python gen.py generate https://video.fastly.steamstatic.com/store_trailers/257121821/movie480_vp9.webm?t=1744279759 --text1 "Try To Drive – Official Co-op Gameplay Trailer" --text2 "Tandem cycling, chaos & teamwork" --cookies cookies.txt --no_facecam
python gen.py generate https://www.youtube.com/watch?v=KK30yerMcsA --text1 "Out of Time" --text2 "New Co op Rouglike" --text3 "" --cookies cookies.txt --no_facecam
DO THIS!!!
f:
cd twitch-
pipenv shell





python gen.py generate https://www.youtube.com/watch?v=SHfjkx1qnSA --text1 "Cronos: The New Dawn" --text2 "Official Gameplay Trailer" --text3 "" --cookies cookies.txt

New singleplayer game where enemies merge into terrifying new forms unless you destroy their bodies—fast. A tense mix of survival horror, time travel, and grotesque strategy.

Explore a brutal sci‑fi survival horror world where time travel and body horror collide. Played from a third‑person view, Cronos: The New Dawn puts you in the shoes of the Traveler, battling grotesque creatures that merge into more powerful abominations unless their corpses are burned immediately.

Developer: Bloober Team  
Release Date: 2025 (Fall—Q3/Q4)  
Platforms: PlayStation 5, Windows PC, Xbox Series X|S


------------

python gen.py generate https://www.youtube.com/watch?v=PDe4NwHJAEQ --text1 "Elden Ring: Nightreign" --text2 "Official Two Player Mode Trailer" --text3 "" --cookies cookies.txt

New singleplayer/coop game now adds two‑player Duo Expeditions mode launching July 30, 2025. Experience the same roguelike action as before but tailored for duos — no more riff‑raff trios or solo struggles.

Explore a procedurally generated parallel of Limgrave—Limveld—where teams of up to three (now two) Nightfarers race through three days of combat, resource gathering, and shrinking safe zones before facing a Nightlord. This new mode delivers tighter, more focused co-op battles without sacrificing the core roguelike intensity of Nightreign.  










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

