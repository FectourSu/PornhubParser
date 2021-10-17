
import pornhub
import youtube_dl
from models.video import VideoModel as Video
from models.items import Item
from extensions.converter import Converter
import random
class PorhnubAPI:
    def __init__(self, categories:str, count_categories:int, count_videos: int):
        # WARNING: garbage code :)
        # mb i'll refact this is garbage
        #TODO: spread by classes
        self.Item.items = Converter.ConvertToList(categories)
        self.categories = random.sample(Item.items, count_categories)
        self.client = pornhub.PornHub(self.categories)
        self.Video.names = [video["name"] for video in self.client.getVideos(count_videos, page = random.randint(0, 10))]
        self.Video.videoUrls = [video["name"] for video in self.client.getVideos(count_videos, page = random.randint(0, 10))]
    
    async def DownloadVideos(names:list, videoUrls:list, path:str):
        for videos in videoUrls:
                names = Video.names
                ydl = youtube_dl.YoutubeDL({'outtmpl': f'{path}/{names}.mp4'})
                with ydl:
                    result = ydl.extract_info(
                        videos,
                        download = True
                    )
                    yield result
