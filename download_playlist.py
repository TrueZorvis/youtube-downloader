# python -m pip install --upgrade pytube

from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PL0k-9Y7O1GweYJHN0QfrW2rUjWxrszsg_')

print(f'{len(playlist.video_urls)} - {playlist.title}')
for count, video in enumerate(playlist.videos):
    print(f'{count+1} - {video.title}')
    try:
        video.streams.get_highest_resolution().download(
            output_path='D:\Videos\YouTube\Front-end Science c Сергеем Пузанковым - GIT'
        )
    except Exception as e:
        print(e)
        raise Exception('Some exception occurred')
    print('Video Downloaded Successfully')
print('All Videos Downloaded Successfully')
