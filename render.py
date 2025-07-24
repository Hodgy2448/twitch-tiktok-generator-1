import math
import subprocess
import os
import textwrap


def extract_resolution(input_file: str) -> tuple[int]:
    cmd = f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {input_file}"
    output = subprocess.run(cmd, shell=True, capture_output=True)
    output = output.stdout.decode()
    width, height = output.split('x')
    return int(width), int(height)


def crop_video(input_file: str, output_file: str, x: int, y: int, w: int, h: int, width: int = 2160, height: int = 2160):
    cmd = f"ffmpeg -y -i {input_file} -filter:v \"crop={w}:{h}:{x}:{y},scale={width}:{height}\" {output_file}"
    subprocess.run(cmd, shell=True)


def scale_video(input_file: str, output_file: str, w: int, h: int):
    cmd = f"ffmpeg -y -i {input_file} -vf scale={w}:{h} {output_file}"
    subprocess.run(cmd, shell=True)


def blur_video(input_file: str, output_file: str, blur: int = 15):
    width, height = extract_resolution(input_file)
    h = height
    w = int(height * 9 / 16)
    x = (width - w) / 2
    y = 0
    cmd = f"ffmpeg -y -i {input_file} -filter:v \"crop={w}:{h}:{x}:{y},boxblur={blur}:1\" {output_file}"
    subprocess.run(cmd, shell=True)


def create_mobile_video(
    background_file,
    content_file,
    facecam_file,
    output_file,
    overlay_text_top=None,
    captions=None,
    blur_strength=15,
    watermark_file=None,
    fps=60,
    voiceover_file=None
):
    _, content_height = extract_resolution(content_file)
    background_width, background_height = extract_resolution(background_file)
    content_x = 0
    content_y = int((background_height - content_height) / 2)

    input_args = f'-i {background_file} -i {content_file}'
    filter_complex = f'[0:v] boxblur={blur_strength}:1 [a]; [a][1:v] overlay={content_x}:{content_y} [b]'
    last_label = 'b'
    input_index = 2

    if facecam_file is not None:
        input_args += f' -i {facecam_file}'
        facecam_width, _ = extract_resolution(facecam_file)
        facecam_x = int((background_width - facecam_width) / 2)
        facecam_y = 0
        filter_complex += f'; [{last_label}][{input_index}:v] overlay={facecam_x}:{facecam_y} [c]'
        last_label = 'c'
        input_index += 1

    if watermark_file:
        input_args += f' -i {watermark_file}'
        filter_complex += (
            f'; [{last_label}][{input_index}:v] scale=500:100,colorchannelmixer=aa=0.5 [wm]; '
            f'[wm] overlay=10:1720 [e]'
        )
        last_label = 'e'
        input_index += 1

    if overlay_text_top:
        wrapped_lines = textwrap.wrap(overlay_text_top, width=25)
        for i, line in enumerate(wrapped_lines):
            safe_text = line.replace("'", r"\'") + "\u00A0\u00A0"
            y_pos = f"h-{3050 - i * 200}"
            filter_complex += (
                f'; [{last_label}]drawtext='
                f"text='{safe_text} ':" 
                f"fontfile=Bangers-Regular.ttf:"
                f"fontcolor=white:fontsize=190:x=(w-text_w)/2+12:y={y_pos}+20:"
                f"borderw=15:bordercolor=black"
                f"[t{i}]"
            )
            last_label = f't{i}'

    if captions:
        for i, (start, end, text) in enumerate(captions):
            words = text.split()
            chunk_size = 3
            num_chunks = math.ceil(len(words) / chunk_size)
            duration = end - start
            chunk_duration = duration / num_chunks

            for j in range(num_chunks):
                chunk_start = start + j * chunk_duration
                chunk_end = chunk_start + chunk_duration
                chunk_words = words[j * chunk_size: (j + 1) * chunk_size]
                chunk_text = " ".join(chunk_words).replace("'", r"\'") + "\u00A0\u00A0"
                y_pos = "h-930"

                filter_complex += (
                    f"; [{last_label}]drawtext="
                    f"text='{chunk_text}':"
                    f"enable='between(t,{chunk_start},{chunk_end})':"
                    f"fontfile=Bangers-Regular.ttf:"
                    f"fontcolor=white:fontsize=180:x=(w-text_w)/2+12:y={y_pos}:"
                    f"borderw=15:bordercolor=black"
                    f"[cap{i}_{j}]"
                )
                last_label = f'cap{i}_{j}'

    if voiceover_file:
        input_args += f' -i {voiceover_file}'
        filter_complex += (
            f'; [{input_index}:a]volume=3.0[vo]; '
            f'[0:a][vo] amerge=inputs=2[aout]'
        )
        audio_map = f'-map "[{last_label}]" -map "[aout]" -ac 2'
    else:
        audio_map = f'-map "[{last_label}]" -map 0:a?'

    cmd = (
        f'ffmpeg -y {input_args} -filter_complex "{filter_complex}" '
        f'{audio_map} -r {fps} '
        f'-c:v h264_nvenc -preset p7 -rc vbr -cq 19 -b:v 0 '
        f'-c:a aac -b:a 192k -pix_fmt yuv420p {output_file}'
    )

    subprocess.run(cmd, shell=True)
