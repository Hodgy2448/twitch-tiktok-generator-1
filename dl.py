import os
from yt_dlp import YoutubeDL

def download(url, output_dir, output_format=None):
    """
    Download a file from a given URL to the specified output directory.

    Args:
        url (str): The URL of the file to download.
        output_dir (str): The directory where the file will be saved.
        output_format (str): The output format (default is best quality up to 1440p).

    Returns:
        str: The full path of the newly downloaded file.
    """
    if output_format is None:
        output_format = 'bestvideo[height<=1440]+bestaudio/best[height<=1440]/best'

    ydl_opts = {
        'format': output_format,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)

    return file_name
