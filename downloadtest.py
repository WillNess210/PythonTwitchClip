import re
import urllib.request
import requests
import sys

basepath = 'downloads/'
base_clip_path = 'https://clips-media-assets2.twitch.tv/'


def retrieve_mp4_data(slug):
    cid = readlines.getAllLinesIn('twitchid.txt')[0]
    clip_info = requests.get(
        "https://api.twitch.tv/helix/clips?id=" + slug,
        headers={"Client-ID": cid}).json()
    thumb_url = clip_info['data'][0]['thumbnail_url']
    title = clip_info['data'][0]['title']
    slice_point = thumb_url.index("-preview-")
    mp4_url = thumb_url[:slice_point] + '.mp4'
    return mp4_url, title


url = "https://clips.twitch.tv/KawaiiRelievedSheepLitFam"
slug = url.split('/')[3].replace('\n', '')
mp4_url, clip_title = retrieve_mp4_data(slug)


regex = re.compile('[^a-zA-Z0-9_]')
clip_title = clip_title.replace(' ', '_')
out_filename = regex.sub('', clip_title) + '.mp4'
output_path = (basepath + out_filename)

urllib.request.urlretrieve(mp4_url, output_path)
print("Done")



