from abc import abstractmethod
from sys import implementation
import pornhub
import os
import youtube_dl
import glob
import asyncio
from models.video import VideoModel as Video
from models.items import Item



# Folder.Clear("Downloads/*")

# if not os.path.exists("Downloads/"):
#     os.mkdir("Downloads")

# def clearTMP(delpath):
#     r = glob.glob(delpath)
#     for i in r:
#         os.remove(i)
    



# async def GetVideos():
#     for video in client.getVideos(10,page=2):
#         Video.name = video["name"]
#         Video.videoUrl = video["url"] + ".mp4"
#         ydl = youtube_dl.YoutubeDL({'outtmpl': f'Downloads/{Video.name}.mp4'})
#         with ydl:
#             result = ydl.extract_info(
#                 Video.videoUrl,
#                 download = True
#             )
#     clearTMP("Downloads/*")

def main():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(GetVideos())


if __name__ == '__main__':
	main()
