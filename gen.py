import os

import fire

from dl import download
from facial_detection import facial_detection, draw_box
from render import crop_video, extract_resolution, blur_video, create_mobile_video
from tts import generate_voiceover


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

    def generate(self, path: str, output: str = 'output', text1: str=None , text2:str =None, text3:str =None,fd_fps: int = 1, blur: int = 20, width=2160, height=3840, no_facecam: bool = False, fps: int = 60, x_offset: int = 0, y_offset: int = 0, cookies: str = None):
        if path.startswith('http'):
            path = download(path, '.', cookies=cookies)
            # if there is a space in the filename, rename
            if ' ' in path:
                new_path = path.replace(' ', '_')
                os.rename(path, new_path)
                path = new_path
            if '&' in path:
                new_path = path.replace('&', '_')
                os.rename(path, new_path)
                path = new_path
            if '|' in path:
                new_path = path.replace('|', '_')
                os.rename(path, new_path)
                path = new_path
        if height % 2 != 0:
            height -= 1
        if width % 2 != 0:
            width -= 1
        output = text1
        if ' ' in output:
                new_output = output.replace(' ', '_')
                output = new_output
        background = f'{output}_background.mp4'
        box = f'{output}_box.mp4'
        facecam = None
        if not no_facecam:
            facecam = f'{output}_face.mp4'
            # get facecam
            x, y, x2, y2 = facial_detection(path, fd_fps)
            w = x2 - x
            h = y2 - y
            output_h = int(height * 0.21875)
            output_w = int(output_h * w / h)
            if output_w % 2 != 0:
                output_w -= 1
            crop_video(path, facecam, x, y, w, h, output_w, output_h)
        # get background
        bg_width, bg_height = extract_resolution(path)
        h = bg_height
        w = int(bg_height * 0.5625)  # 9/16 in decimal
        x = (bg_width - w) / 2
        y = 0
        crop_video(path, background, x, y, w, h, width, height)
        # get the center 1:1 content of the video
        x = (bg_width - bg_height) / 2 + x_offset + 50
        y = 0 + y_offset
        w = bg_width
        h = bg_height
        box_scale = 1
        box_width = int(width * box_scale)
        box_height = int(width * box_scale) - 700

        # Ensure dimensions are even (required by many codecs)
        if box_width % 2 != 0:
            box_width -= 1
        if box_height % 2 != 0:
            box_height -= 1

        crop_video(path, box, x, y, w, h, box_width, box_height)
        voice_path = None
        if text3:
            voice_path = f"{output}_voice.mp3"
            generate_voiceover(text3, voice_path)

        create_mobile_video(background, box, facecam,
                            f'{output}.mp4', text1, text2, blur_strength=blur, fps=fps, voiceover_file=voice_path)
        if not no_facecam:
            os.remove(facecam)
        os.remove(background)
        os.remove(box)
        os.remove(path)
        os.remove(voice_path)

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
