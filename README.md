



ː colon



DO THIS!!!
f:
cd twitch-
pipenv shell

python gen.py generate https://www.twitch.tv/thaqil/clip/ImpartialAnimatedClipzNomNom-JnLk34HYv3sNGbVC --output tiktokclip --text "THIS GUY IS SO BAD"
--------------------------------------
python gen.py generate https://www.youtube.com/watch?v=M6vsxYyQZnA --text1 "Echoes of the End - Announcement Trailer" --text2 "New action-adventure game" --cookies cookies.txt --no_facecam


New action-adventure game! Coming out soon!

Embark on a perilous journey to rescue your brother and prevent a looming war. Harness the power of devastating magical abilities to conquer enemies, traverse treacherous landscapes, and unveil the hidden history of Aema.

Developer: Myrkur Games
Release Date: Coming to PlayStation 5 (PS5), Xbox Series X|S, and PC (Steam) on 12 Aug, 2025
--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=uvZDdYWmgLc --text1 "Atmosfar - Official Announcement Trailer" --text2 "New open-world survival with friends" --cookies cookies.txt --no_facecam


New open-world survival game!

ATMOSFAR is a sky-high odyssey set on an alien planet of floating islands explored by flying crafts and a mobile airbase as you uncover the fate of your collapsed colony.

Developer: Apog Labs
Release Date: Coming to  PC (Steam) in 2026, wishlist on Steam now!
--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=oozm6uOZm9c --text1 "Stormforge - Official Gameplay Trailer" --text2 "New open-world survival with friends" --cookies cookies.txt --no_facecam


New open-world survival game!

Stormforge is an open-world survival crafting game for 1 to 8 players. You are Stormforged, with the ability to brave and harness power from magical storms. Explore, fight, forage, craft, build, and defeat bosses in this epic, fantasy game. Survive the Storms and thrive!

Developer: Roboto Games
Release Date: TBA, wishlist on Steam now!

--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=8g7pBKlZ_ow --text1 "Inkwellers - Official Trailer" --text2 "New two-player co-op puzzle game" --cookies cookies.txt --no_facecam


New co-op puzzle game!

In this Online 2 player co-op puzzle adventure game, you and a friend become Inkwellers - story dwellers diving into Celiphia’s journal. Solve puzzles, explore forgotten memories, and uncover the truth behind her mysterious disappearance.

Developer: @ScrumptiousSprouts
Release Date: 2025, wishlist on Steam now!
--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=zIaMXjT_Nvk --text1 "Ikumaː The Frozen Compass - Official Reveal Trailer" --text2 "New two-player couch adventure game" --cookies cookies.txt --no_facecam


New co-op couch game!

Embark on a haunting journey into the cold in this narrative adventure - either alone or with a friend. IKUMA tells the story of Sam, a teenage boy who finds himself stranded in the Arctic with his dog. He must face not only its harsh environment, but also something lurking deeper in the shadows.

Developer: Mooneye Studios
Release Date: PC, PS5 (PlayStation 5), and Xbox Series X/S in 2026, wishlist on Steam now!
--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=2fbH7iWdJjs --text1 "IfSunSets - Official Early Access Gameplay Trailer" --text2 "Co op game to play with friends" --cookies cookies.txt --no_facecam


It's not new but worth sharing!

「IfSunSets」 is a survival RPG adventure game. During the day, secure necessary supplies across the island, and survive the night against strong and terrifying monsters that track you down. You can utilize resources you've secured to build a base to fend off threatening monsters.

Developer: POLYMORPH
Release Date: Early Access Game on PC (Steam)!
--------------------------------------------
python gen.py generate https://www.youtube.com/watch?v=rcxnRaZ6slU --text1 "Star Wars Zero Company | Official Announce Trailerr" --text2 "New star wars game" --cookies cookies.txt --no_facecam


New Star Wars game!

Command an elite squad through a gritty and authentic story in STAR WARS Zero Company™, a single-player turn-based tactics game set in the twilight of the Clone Wars.

Developer: Bit Reactor
Release Date: Coming 2026!









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

