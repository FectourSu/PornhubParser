
import pornhub
import youtube_dl
from models.video import VideoModel as Video
from models.items import Item

class PorhnubAPI:
    def __init__(self):
        Item.items = ["Big Ass", "Big Tits"]
        client = pornhub.PornHub(keywords=["Big Ass", "Big Tits"])
        Video.names = [video["name"] for video in client.getVideos(10, page = 2)]
        Video.videoUrls = [video["name"] for video in client.getVideos(10, page = 2)]

    async def DownloadVideos(names:list, videoUrls:list):
        for videos in videoUrls:
                names = Video.names
                ydl = youtube_dl.YoutubeDL({'outtmpl': f'Downloads/{names}.mp4'})
                with ydl:
                    result = ydl.extract_info(
                        videos,
                        download = True
                    )