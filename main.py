from twitch import TwitchClient
import json
import re
import urllib.request
import requests
import sys
import readlines
#SETTINGS
cid = readlines.getAllLinesIn('twitchid.txt')[0]
print(cid)
client = TwitchClient(client_id=cid)
result = client.clips.get_top(None, None, 'Fortnite', None, 3, 'day')
downloadloc = 'downloads/'

def get_mp4_data(slug):
    clipinfo = client.clips.get_by_slug(slug)
    title = clipinfo['title']
    vidurl = clipinfo['thumbnails']['medium']
    slicept = vidurl.index("-preview-")
    mp4url = vidurl[:slicept] + '.mp4'
    return mp4url, title

def downloadClip(url):
    slug = url.split('/')[3].replace('\n', '')
    mp4url, cliptitle = get_mp4_data(slug)
    regex = re.compile('[^a-zA-Z0-9_]')
    cliptitle = cliptitle.replace(' ', '_')
    out_filename = regex.sub('', cliptitle) + '.mp4'
    output_path = (downloadloc + out_filename)
    urllib.request.urlretrieve(mp4url, output_path)
    print("Downloaded " + cliptitle)


# MAIN CODE
urls = []
for i in result:
    urls.append(i['url'].split('?')[0])
for i in urls:
    downloadClip(i)





