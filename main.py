#!/usr/bin/env python3
import time
import argparse
import subprocess
import os

parser = argparse.ArgumentParser()
parser.add_argument("-v", dest='video', default="https://www.youtube.com/watch?v=dQw4w9WgXcQ", help="YouTube video URL")
parser.add_argument("-d", dest='dongle', default="search_it", help="Device URL")

args = parser.parse_args()

ydl_opts = {}
subprocess.call(['rm', '-rf', 'video.mp4'])

f = open("stream.pid", "r")
subprocess.call(['kill', f.read()])

subprocess.call(['yt-dlp', '-f', 'bv*+ba', '--merge-output-format', 'mp4', args.video, '-o', 'video.mp4'])
p = subprocess.Popen(['nanodlna', 'play', "video.mp4", '-d', args.dongle])
f = open("stream.pid", "w")
f.write("{}".format(p.pid))
f.close()
