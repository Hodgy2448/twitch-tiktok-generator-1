import os
from yt_dlp import YoutubeDL

def download(url, output_dir, output_format=None, cookies=None):
    if output_format is None:
        output_format = 'bestvideo[height<=1440]+bestaudio/best[height<=1440]/best'

    ydl_opts = {
        'format': output_format,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }
    
    if cookies:
        ydl_opts['cookiefile'] = cookies

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)

    return file_name
