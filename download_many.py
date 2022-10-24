# python -m pip install --upgrade pytube

from pytube import YouTube

list_urls = [
    '',
    ''
]

for url in list_urls:
    try:
        yt_obj = YouTube(url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        filters.get_highest_resolution().download(output_path='D:\Videos\YouTube')
    except Exception as e:
        print(e)
        raise Exception('Some exception occurred')
print('All Videos Downloaded Successfully')
