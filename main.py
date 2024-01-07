from pytube import YouTube
from moviepy.editor import *

url = input('Enter song url from Youtube :\t')
load = YouTube(url)
video = load.streams.filter(only_audio=True).first()
video.download(filename = 'temp')

name = input('Enter a name for the file :\t')

converted_video = AudioFileClip('temp')
if len(name) > 0: 
  converted_video.write_audiofile(name + ".mp3")
else:
  converted_video.write_audiofile('output.mp3')