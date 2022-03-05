#!/usr/bin/env python3
import time
import argparse
import subprocess
import os
import json


parser = argparse.ArgumentParser()
parser.add_argument("-v", dest='video', default="https://www.youtube.com/watch?v=dQw4w9WgXcQ", help="YouTube video URL")
parser.add_argument("-d", dest='dongle', default="search_it", help="YouTube video URL")

args = parser.parse_args()

ydl_opts = {}
subprocess.call(['rm', '-rf', 'video.mp4'])
subprocess.call(['rm', '-rf', 'video.*.webm'])

f = open("stream.pid", "r")

subprocess.call(['kill', f.read()])

subprocess.call(['yt-dlp', '--write-info-json', args.video, '-o' 'info'])

# read file
with open('info.info.json', 'r') as myfile:
    data=myfile.read()

# parse file
data = json.loads(data)
subprocess.call(['yt-dlp', '-f', 'bv*+ba', '--merge-output-format', 'mp4', args.video, '-o', 'video.mp4'])
p = subprocess.Popen(['nanodlna', 'play', "video.mp4", '-d', 'http://192.168.1.122:1829/', '-s', data['title']])
f = open("stream.pid", "w")
f.write("{}".format(p.pid))
f.close()
