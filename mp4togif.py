from moviepy.editor import *

clip = VideoFileClip("downloads/clip1.mp4")
clip.write_gif('downloads/clip1.gif')