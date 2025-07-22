



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

python gen.py generate https://video.fastly.steamstatic.com/store_trailers/257161242/movie480_vp9.webm?t=1750847500 --text1 "Scoot – Official Trailer" --text2 "show off your crazy stunts" --text3 "Get ready to shred harder than ever. This is Scoot, the most advanced scooter game on PC—satisfyingly realistic, but fun enough for everyone. Powered by sim-cade physics, Scoot lets you gap massive stair sets, conquer bowls, nail insane tricks over mega-ramps, or link combos mid-air seamlessly. With over 40 unique tricks and fully re-worked animations, you can pull off jaw-dropping lines while keeping total control. Explore New Carven’s gritty street spots, or take off to Jumbo Jump Island’s downhill paradise. Prefer to build? The Park Builder lets you design killer skateparks with endless rails, bowls, and big jumps to test your skills. Ride solo, shred online with up to four friends in public or private lobbies, film your combos with the Replay Editor, then customize your rider and scooter to show your style. Scoot — experience the thrill of scooter riding like never before. Now available on Steam. Time to ride." --cookies cookies.txt --no_facecam

Scoot is an extreme scooter game packed with fast tricks, huge ramps, and wild environments. Pull off insane combos and challenge your friends to become the ultimate scooter pro.

Developer: Tank Media  
Release Date: September 2025  
Platforms: PC (Steam)

------------
python gen.py generate https://www.youtube.com/watch?v=fEolJAuuIco --text1 "SurrounDead – Official Trailer" --text2 "New unturned 2.0??" --cookies cookies.txt --no_facecam

SurrounDead is an open-world survival game set in a post-apocalyptic world overrun by zombies. Scavenge for resources, build shelters, and fight to stay alive in a harsh, unforgiving environment.

Developer: Zurvivor  
Release Date: June 24, 2022  
Platforms: PC (Steam)









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

