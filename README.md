## Download any video on YouTube by terminal

## Dependencies:

```python
pip install pytube
pip install os_sys
```

## To download songs use:

```python
python3 yt.py -s

Please, paste the Youtube video url: your-url-video
```

## To download videos use `-v` flag

## Bug solved!

### For solve the error `get_throttling_function_name: could not find match for multiple` open `pytube > cipher.py` and in `get_throttling_function_name` function replace `function_patterns` by:

```python
     function_patterns = [r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)']
```

### Demonstration:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/84200694/207482693-bf3a7c8c-c7ce-4291-9bc3-cfc493c8c457.gif)

### 🚦 You need python3 installed! `I used Python 3.10.8 version`

### Installation:

`git clone https://github.com/josephbrito/YouTubeVideoDownload.git`

`cd YouTubeVideoDownload`

`python3 yt.py`
