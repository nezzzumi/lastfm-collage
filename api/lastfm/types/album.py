from typing import List

from api.lastfm.types.artist import Artist
from api.lastfm.types.image import Image


class Album:
    def __init__(self, artist: Artist, image: List[Image], mbid: str, url: str, playcount: str, name: str) -> None:
        self.artist = artist
        self.images = image
        self.mbid = mbid
        self.url = url
        self.playcount = int(playcount)
        self.name = name

    def as_dict(self) -> dict:
        return {
            "artist": self.artist.name,
            "name": self.name
        }
