from pytube import YouTube
import sys
import os

def LoadingDownload(stream, chunk, bytes):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

yt = YouTube(input("Please, paste the Youtube video url: "), on_progress_callback=LoadingDownload)
    
def DownloadVideo():
    try:
        if sys.argv[1] == "-s":
            video = yt.streams.filter(only_audio=True).first()
            destination = '.'
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            return
        else:
            yt.streams.get_highest_resolution().download()
            print("Video downloaded")
            return
            
    except Exception as e:
        print("An error ocurred: ")
        print(e)
        return

DownloadVideo()