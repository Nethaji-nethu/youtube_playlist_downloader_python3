import sys
try:
    from pytube import Playlist
except ImportError as err:
    print('Please install the pytube package first using the below command')
    print('pip3 install pytube # if you are using python 3')
    print('pip install pytube # if you are using python 2')
    sys.exit(0)

#give the playlist here
pl = Playlist(input('Enter the playlist URL : '))

print(pl.title)

print(len(pl.video_urls), 'videos are present')

# To save it in a directory, uncomment the commented below

##downloads_dir = 'C:\\Users\\Nethaji\\Docker and Kube tutorial'
##for video in pl.videos:
##        video.streams.\
##        filter(type='video', progressive=True, file_extension='mp4').\
##        order_by('resolution').\
##        desc().\
##        first().\
##        download(downloads_dir)
##        print(video.title , '.'*50 , 'Downloaded')

#To save it in current directory of this program, use below

for video in pl.videos:
        video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download()
        print(video.title , '.'*50 , 'Downloaded')
