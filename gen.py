import os
import re
import unicodedata

import fire

from dl import download
from facial_detection import facial_detection, draw_box
from render import crop_video, extract_resolution, blur_video, create_mobile_video
from tts import generate_voiceover_with_captions, merge_voiceover_with_video_audio


class TikTokGenerator:
    def detect(self, path: str, fps: int = 1, box: bool = False):
        x, y, x2, y2 = facial_detection(path, fps)
        print(f"Top Left: {x} {y}")
        print(f"Bottom Right: {x2} {y2}")
        if box:
            for image_path in os.listdir('thumbs'):
                draw_box(f'thumbs/{image_path}', x, y, x2, y2)

    def crop_face(self, path: str, fps: int = 1):
        x, y, x2, y2 = facial_detection(path, fps)
        w = x2 - x
        h = y2 - y
        crop_video(path, 'output.mp4', x, y, w, h)

    def crop_box(self, path: str):
        width, height = extract_resolution(path)
        # get the center 1:1 box of the video
        x = (width - height) / 2
        y = 0
        w = height
        h = height
        crop_video(path, 'output.mp4', x, y, w, h)

    def blur(self, path: str, blur: int = 15):
        blur_video(path, 'output.mp4', blur)

    def is_text1_in_filenames(self, text1: str = None, folder='.'):

        def sanitize(text):
            if not text:
                return ''
            # Normalize Unicode (e.g., full-width to ASCII)
            text = unicodedata.normalize('NFKC', text)
            # Replace forbidden/unsafe characters with _
            return re.sub(r'[\\/:*?"<>|&\s]', '_', text)

        text1_sanitized = sanitize(text1)

        for filename in os.listdir(folder):
            if text1_sanitized in sanitize(filename):
                return True, filename
        return False, None

    def generate(self, path: str, output: str = 'output', text1: str=None , text2:str =None, text3:str =None, blur: int = 20, width=2160, height=3840, fps: int = 60, cookies: str = None):
        exists, matched_file = self.is_text1_in_filenames(text1)
        if exists:
            print(f"File found matching text1: {matched_file}")
            path = matched_file
            invalid_chars = [':', '：', ' ', '&', '|']
            for char in invalid_chars:
                if char in path:
                    new_path = path.replace(char, '_')
                    os.rename(path, new_path)
                    path = new_path
        else:
            print("No file matching text1 found.")
            if path.startswith('http'):
                path = download(path, '.', cookies=cookies)
                # if there is a space in the filename, rename
                invalid_chars = [':', '：', ' ', '&', '|']
                for char in invalid_chars:
                    if char in path:
                        new_path = path.replace(char, '_')
                        os.rename(path, new_path)
                        path = new_path
            print(f"Downloaded file path: {path}")
        if height % 2 != 0:
            height -= 1
        if width % 2 != 0:
            width -= 1
        if text1 and text1.strip():
            output = text1 + '_' + text2
            invalid_chars = [':', '：', ' ', '&', '|']
            for char in invalid_chars:
                if char in output:
                    output = output.replace(char, '_')

            background = f'{output}_background.mp4'
            box = f'{output}_box.mp4'
            intermediate_output = f'{output}_premerge.mp4'

            invalid_chars = [':', '：']
            for char in invalid_chars:
                if char in text1:
                    text1 = text1.replace(char, 'ː')
            print(text1)
        else:
            text1 = None
            text2 = None
            text3 = None
            background = 'test_background.mp4'
            box = 'test_box.mp4'
            intermediate_output = 'test_premerge.mp4'
        # get background
        if(not os.path.exists(background)):
            bg_width, bg_height = extract_resolution(path)
            h = bg_height
            w = int(bg_height * 0.5625)  # 9/16 in decimal
            x = (bg_width - w) / 2
            y = 0
            crop_video(path, background, x, y, w, h, width, height)
        # get box
        if(not os.path.exists(box)):
            square_size = min(bg_width, bg_height)
            x = (bg_width - square_size) // 2
            y = (bg_height - square_size) // 2
            box_width = 2160
            box_height = 2160
            crop_video(path, box, x, y, square_size, square_size, box_width, box_height)
        voice_path = None
        captions = None
        delay=3.0
        if text3 and text3.strip():
            voice_path = f"{output}_voice.mp3"
            voice_captions =f"{output}_captions.srt"
            if(not os.path.exists(voice_path)):
                voice_path, captions = generate_voiceover_with_captions(text3, audio_path=voice_path, srt_path=voice_captions, delay=delay)

        create_mobile_video(
            background_file=background,
            content_file=box,
            output_file=intermediate_output,
            overlay_text_top=text1,
            overlay_text_bottom=text2,
            captions=captions,
            blur_strength=blur,
            fps=fps,
            voiceover_file=None
        )
        if voice_path:
            merge_voiceover_with_video_audio(intermediate_output, voice_path, f'{output}.mp4', delay=delay)
            os.remove(intermediate_output)
        else:
            os.rename(intermediate_output, f'{output}.mp4')
        
        os.remove(background)
        os.remove(box)
        os.remove(path)
        if voice_path:
            os.remove(voice_path)
        if text3:
            os.remove(voice_captions)

    def blur_box(self, path: str, output: str = 'output', blur: int = 20, width=1080, height=1920, fps: int = 60):
        '''Takes a square video, blurs it, makes it 9:16, then add the original video on top of it'''
        if height % 2 != 0:
            height -= 1
        if width % 2 != 0:
            width -= 1
        background = f'{output}_background.mp4'
        # get background
        bg_width, bg_height = extract_resolution(path)
        h = bg_height
        w = int(bg_height * 0.5625)  # 9/16 in decimal
        x = (bg_width - w) / 2
        y = 0
        if not os.path.exists(background):
            crop_video(path, background, x, y, w, h, width, height)
        # no need to get the center 1:1 content of the video
        # since its already a square
        create_mobile_video(background, path, None,
                            f'{output}.mp4', blur_strength=blur, fps=fps)
        os.remove(background)

    def extract(self, input_file: str):
        '''Extracts the center 9:16 portion of the video'''
        width, height = extract_resolution(input_file)


if __name__ == '__main__':
    fire.Fire(TikTokGenerator)
