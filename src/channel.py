import os
from pprint import pprint

from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id: str = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # print(Channel.api_key)
        youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pprint(channel)
