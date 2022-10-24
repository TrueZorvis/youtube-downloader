# python -m pip install --upgrade pytube

from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=PDCLoE-xOWM'

try:
    yt_obj = YouTube(youtube_video_url)
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    filters.get_highest_resolution().download(output_path='D:\Videos\YouTube')
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
