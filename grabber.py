import asyncio
import pornhub
import youtube_dl
from youtube_dl.postprocessor.ffmpeg import FFmpegExtractAudioPP, FFmpegFixupM3u8PP, FFmpegFixupM4aPP
from models.video import VideoModel as Video
from models.items import Item
from extensions.converter import Converter
import random
import os

class PorhnubAPI:
    def __init__(self, categories_list:str, path:str, count:int):
        # WARNING: garbage code :)
        # mb i'll refact this is garbage
        #TODO: spread by classes
        self.path = path
        Item.items = Converter.ConvertToList(categories_list)
        self.categories = random.sample(Item.items, random.randint(0, 10))
        self.client = pornhub.PornHub(self.categories)
        self.videos = self.client.getVideos(count, page = random.randint(0, 10))
        
    async def download(self):
        try:
            for video in self.videos:
                    Video.names = video["name"]
                    Video.videoUrls = video["url"]
                    ydl = youtube_dl.YoutubeDL({
                        'outtmpl': f'{self.path}/{Video.names}.mp4',
                        })
                    with ydl:
                        result = ydl.extract_info(
                            Video.videoUrls,
                            download = True
                        )
                                                
        except Exception as ex:
            print(ex)
            raise Exception
    
    async def get_categories(self):
        return [category.replace(' ', '') for category in self.categories]
    
    #tags categories such as -> #Japanese
    def get_tags(self, categories:list):
        return " ".join(str('#' + x) for x in [category.replace(' ', '') for category in categories])