#!*python_path*

from pytube import YouTube
import sys
import os

def LoadingDownload(stream, chunk, bytes):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


def DownloadVideo():

    if len(sys.argv) != 3:
        print('Usage: python youtube.py [option] [url]')
        return
    midia_format = sys.argv[1]
    url = sys.argv[2]
    yt = YouTube(url, on_progress_callback=LoadingDownload)

    try:
        if midia_format == "-s":
            video = yt.streams.filter(only_audio=True).first()
            destination = os.path.join('/Users/josebrito', 'youtube')
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            return
        elif midia_format == "-v":
            destination = os.path.join('/Users/josebrito', 'youtube')
            yt.streams.get_highest_resolution().download(output_path=destination)
            print("Video downloaded")
            return
        else:
            print('Usage: python youtube.py [option] [url]')
            return
    except Exception as e:
        print("An error ocurred: ")
        print(e)
        return

DownloadVideo()