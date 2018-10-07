from os import listdir
from os.path import isfile, join
from moviepy.editor import VideoFileClip, concatenate_videoclips
'''
mypath = "downloads"
files = listdir(mypath)
print(files)

#concatenation
clips = []
for filename in files:
	path = "downloads/" + filename
	print(path)
	clips.append(VideoFileClip(path))

final = concatenate_videoclips(clips)
final.write_videofile("downloads/final.mp4")
'''

clip1 = VideoFileClip("downloads/clip1.mp4")
clip2 = VideoFileClip("downloads/clip2.mp4")
clip12 = concatenate_videoclips([clip1,clip2])
clip3 = VideoFileClip("downloads/clip3.mp4")
clip4 = VideoFileClip("downloads/clip4.mp4")
clip5 = VideoFileClip("downloads/clip5.mp4")
clip345 = concatenate_videoclips([clip3, clip4, clip5])
final_clip = concatenate_videoclips([clip12, clip345])
final_clip.write_videofile("my_concatenation.mp4")

