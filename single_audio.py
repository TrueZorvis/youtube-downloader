# python -m pip install --upgrade pytube

from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=Z7AY41tE-3U'

try:
    yt_obj = YouTube(youtube_video_url)
    yt_obj.streams.get_audio_only().download(output_path='/mnt/data/YouTube', filename='audio.mp3')
    print('Audio Downloaded Successfully')
except Exception as e:
    print(e)
