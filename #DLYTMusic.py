'''
reqs:
pip install yt-dlp moviepy
read file line by line
download each file
convert mp4 to mp3
delete mp4
profit

include -p for inputting playlists.
'''
import os
import sys
import platform
from os import listdir
from os.path import isfile, join
from moviepy.editor import *

def helpText():
    print("Usage: script.py <fileName> -- if no filename permitted, will just convert mp4 to mp3")
    exit()

def getFile(path):
    inf = open(path, 'r')
    names = inf.readlines()
    for name in range(len(names)):  # get /n outta there
        names[name] = names[name][:-1]
    inf.close()
    return names

def MP4toMP3(mp4, mp3):
    x = AudioFileClip(mp4)
    x.write_audiofile(mp3)
    x.close()

def main():
    mp4Files = []
    command = 'del "'
    if(len(sys.argv) > 3):
        helpText()
    #do some youtube downloading 
    if(len(sys.argv) == 2):
        fileName = './' + sys.argv[1]
        if not os.path.isfile(fileName):
            print("file doesn't exist")
            helpText()
        URLs = getFile(fileName)
        for URL in URLs:
            os.system("yt-dlp " + URL)
    if(len(sys.argv) == 3):
        os.system("yt-dlp " + sys.argv[2])
    #List all MP4s
    allFiles = [f for f in listdir('./') if isfile(join('./', f))]
    if len(allFiles) == 0:
        helpText()
    for file in allFiles:
        if(file[-3:] == 'mp4'):
            mp4Files.append(file)
    if platform.system() == 'Linux': command = 'rm "'
    #convert to mp3
    for file in mp4Files:
        MP4toMP3(file, file[:-1]+'3')
        os.system(command + file + '"')
    

if __name__ == "__main__":
    main()

