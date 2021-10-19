from typing import Text
import asyncio
import sys
from helpers.folder import Folder
from grabber import PorhnubAPI
from extensions.module_installer import Module
from models.video import VideoModel as Video
from models.items import Item
from helpers.folder import Folder

CATEGORIES = "categories.txt"
MODULES = MODULES = {
    "youtube_dl" : "youtube_dl",
    "requests" : "requests",
    "ffmpeg" : "ffmpeg",
    "asyncio" : "asyncio",
    "glob" : "glob",
    "csv" : "csv",
    "pyinstaller" : "pyinstaller",
}
FOLDER = Folder.Create("downloads")


async def installpack():
    print("\n [+] Checking requred packages")
    for i in MODULES: # Will run untill all the packages has been installed and imported successfully
        if (i in sys.modules) == False:
            Module.install(i)
        else:
            print(f" [+] Package {i} installed")
            

def main():
    #if you want auto-clean remove '#' from below
    Folder.Clear(f"{FOLDER}/*")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(installpack())

    print("\nEnter count FULL videos(0 to 10): ")
    video_count = int(input())
   
    if video_count < 0 and video_count > 10: return #easy dodge

    api = PorhnubAPI(CATEGORIES, FOLDER, video_count)
    loop.run_until_complete(api.download())


if __name__ == '__main__':
	main()
