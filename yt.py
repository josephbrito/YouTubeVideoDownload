from pytube import YouTube

def LoadingDownload(stream, chunk, bytes):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

    
def DownloadVideo(url):
    try:
        yt = YouTube(url, on_progress_callback=LoadingDownload)
        yt.streams.get_highest_resolution().download()
        print("Video downloaded")
    except Exception as e:
        print("An error ocurred: ")
        print(e)

url = input("Please, paste the Youtube video url: ")
DownloadVideo(url)