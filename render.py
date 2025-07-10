import subprocess
import os
import textwrap


def extract_resolution(input_file: str) -> tuple[int]:
    cmd = f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {input_file}"
    output = subprocess.run(cmd, shell=True, capture_output=True)
    output = output.stdout.decode()
    width, height = output.split('x')
    return int(width), int(height)


def crop_video(input_file: str, output_file: str, x: int, y: int, w: int, h: int, width: int = 608, height: int = 608):
    cmd = f"ffmpeg -y -i {input_file} -filter:v \"crop={w}:{h}:{x}:{y},scale={width}:{height}\" {output_file}"
    subprocess.run(cmd, shell=True)


def scale_video(input_file: str, output_file: str, w: int, h: int):
    cmd = f"ffmpeg -y -i {input_file} -vf scale={w}:{h} {output_file}"
    subprocess.run(cmd, shell=True)


def blur_video(input_file: str, output_file: str, blur: int = 15):
    '''crops the center 9:16 portion of the video and blurs'''
    width, height = extract_resolution(input_file)
    h = height
    w = int(height * 9 / 16)
    x = (width - w) / 2
    y = 0
    # crop and blur in one command
    cmd = f"ffmpeg -y -i {input_file} -filter:v \"crop={w}:{h}:{x}:{y},boxblur={blur}:1\" {output_file}"
    subprocess.run(cmd, shell=True)


def create_mobile_video(background_file, content_file, facecam_file, output_file, overlay_text_top=None, overlay_text_bottom=None, blur_strength=15, watermark_file=None, fps=60):
    _, content_height = extract_resolution(content_file)
    background_width, background_height = extract_resolution(background_file)
    content_x = 0
    content_y = int((background_height - content_height) / 2)
    input_args = f'-i {background_file} -i {content_file}'
    filter_complex = f'[0:v] boxblur={blur_strength}:1 [a]; [a][1:v] overlay={content_x}:{content_y} [b]'
    last_label = 'b'

    if facecam_file is not None:
        facecam_width, _ = extract_resolution(facecam_file)
        facecam_x = int((background_width - facecam_width) / 2)
        facecam_y = 0
        input_args += f' -i {facecam_file}'
        filter_complex += f'; [b][2:v] overlay={facecam_x}:{facecam_y} [c]'
        last_label = 'c'

    if watermark_file:
        input_args += f' -i {watermark_file}'
        filter_complex += f'; [{last_label}][3:v] scale=500:100,colorchannelmixer=aa=0.5 [d]; [d] overlay=10:1720 [e]'
        last_label = 'e'

    if overlay_text_top:
        wrapped_lines = textwrap.wrap(overlay_text_top, width=30)  # adjust width
        for i, line in enumerate(wrapped_lines):
            safe_text = line.replace("'", r"\'") + "\u00A0\u00A0"
            y_pos = f"h-{1550 - i * 80}"
            filter_complex += (
                f'; [{last_label}]drawtext='
                f"text='{safe_text} ':"
                f"fontfile=Bangers-Regular.ttf:"
                f"fontcolor=white:fontsize=90:x=(w-text_w)/2:y={y_pos}:"
                f"borderw=5:bordercolor=black;"
                f"[t{i}]"
            )
            last_label = f't{i}'

    if overlay_text_bottom:
        wrapped_lines = textwrap.wrap(overlay_text_bottom, width=30)  # adjust width
        for i, line in enumerate(wrapped_lines):
            safe_text = line.replace("'", r"\'") + "\u00A0\u00A0"
            y_pos = f"h-{450 - i * 80}"
            filter_complex += (
                f'; [{last_label}]drawtext='
                f"text='{safe_text} ':"
                f"fontfile=Bangers-Regular.ttf:"
                f"fontcolor=white:fontsize=80:x=(w-text_w)/2:y={y_pos}:"
                f"borderw=5:bordercolor=black"
                f"[b{i}]"
            )
            last_label = f'b{i}'

    cmd = (
        f'ffmpeg -y {input_args} -filter_complex "{filter_complex}" '
        f'-map "[{last_label}]" -map 0:a? -r {fps} -c:v libx264 -c:a aac -pix_fmt yuv420p {output_file}'
    )

    subprocess.run(cmd, shell=True)

