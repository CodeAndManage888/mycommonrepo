# Code from social media - YouTube
# YouTube Downloader | Status: Working
# How to Use: 
# a. Run code in the terminal and add the youtube link to download.
#    command line: python3 <programname.py> <youtube link>
# b. Modify the code to remove the use of argv and hardcode the link
#    then run the program to any IDE.
# ---------------------------------------------------------------------

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

#yd.download('/home/pi/Desktop/Programming Projects/Python/Program Files/Output')
yd.download('/home/pi/Desktop/youtube')

# ---------------------------------------------------------------------
# Other Use Cases:
# ---------------------------------------------------------------------
# a. Extact youtube video information for data analytics purposes
# b. Can you analyze youtube history and activities?