## Download any video on YouTube by terminal

## Dependencies:

```python
pip install pytube
pip install os_sys
```

## To download songs use:

```python
python3 yt.py -s your_url

Please, paste the Youtube video url: your-url-video
```

## To download videos use:

```python
python3 yt.py -v your_url
```

## Solving some bugs

### For solve the error `get_throttling_function_name: could not find match for multiple` open `pytube > cipher.py` and in `get_throttling_function_name` function replace `function_patterns` by:

```python
     function_patterns = [r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)']
```

### Another common error's age restricted. For solve it open `pytube > innertube.py` and at line 223 change `ANDROID_MUSIC` to `ANDROID` as below:

```python
def __init__(self, client='ANDROID_MUSIC', use_oauth=False, allow_cache=True):

def __init__(self, client='ANDROID', use_oauth=False, allow_cache=True):
```

## Make it globally

```shell
cp yt.py /usr/local/bin/youtube
chmod 544 /usr/local/bin/youtube
```

### Demonstration:

![GravaodeTela2024-03-21s10 28 48-ezgif com-video-to-gif-converter](https://github.com/josephbrito/YouTubeVideoDownload/assets/84200694/5122ea36-eeb3-4c51-9938-91d45e57895d)

### 🚦 You need python3 installed! `I used Python 3.10.8 version`

### Installation:

`git clone https://github.com/josephbrito/YouTubeVideoDownload.git`

`cd YouTubeVideoDownload`

`python3 yt.py`
