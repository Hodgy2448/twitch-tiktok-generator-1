



ː colon

python gen.py generate https://www.twitch.tv/thaqil/clip/ImpartialAnimatedClipzNomNom-JnLk34HYv3sNGbVC --output tiktokclip --text "THIS GUY IS SO BAD"
python gen.py generate https://video.fastly.steamstatic.com/store_trailers/257121821/movie480_vp9.webm?t=1744279759 --text1 "Try To Drive – Official Co-op Gameplay Trailer" --text2 "Tandem cycling, chaos & teamwork" --cookies cookies.txt --no_facecam

DO THIS!!!
f:
cd twitch-
pipenv shell





python gen.py generate https://www.youtube.com/watch?v=j9zHZK4zDnk --text1 "Eldramoorː Haven in the Mist" --text2 "new VRMMORPG game" --cookies cookies.txt --no_facecam

Experience a wild, fantastic landscape full of wonders, secrets, and the scars of a troubled history. Join friends old and new for fierce combat, clever crafting, deep customization, and a sprawling story that spans generations

Developer: Resolute Games, Inc. 
Release Date: TBA
Platforms: VR

-----------------

python gen.py generate https://video.fastly.steamstatic.com/store_trailers/257161242/movie480_vp9.webm?t=1750847500 --text1 "Scoot – Official Trailer" --text2 "Get ready to shred with Scoot, the ultimate scooter game on PC. Realistic physics, arcade-style fun. Nail insane tricks, gap stair sets, and dominate bowls with over 40 tricks and smooth, reworked animations. Explore gritty city spots or go huge on downhill mega-ramps. Build your own parks with rails, bowls, and jumps using the Park Builder. Play solo or with friends online. Record your best runs, customize your setup, and show off your style. Scoot—ride big, land clean, and make it yours. Available now on Steam." --cookies cookies.txt --no_facecam

Scoot is an extreme scooter game packed with fast tricks, huge ramps, and wild environments. Pull off insane combos and challenge your friends to become the ultimate scooter pro.

Developer: Tank Media  
Release Date: September 2025  
Platforms: PC (Steam)














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

