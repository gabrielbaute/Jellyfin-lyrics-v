from typing import List
from pydantic import BaseModel, ConfigDict

class TrackModel(BaseModel):
    """
    Data models for a track, used for fetching lyrics from LRCLib.

    Attributes:
        title (str): Title of the track.
        artists (List[str]): List of artists.
        album (str): Album name.
        duration_seconds (int): Duration of the track in seconds.
    """
    title: str
    artists: List[str] = []
    album: str
    duration_seconds: int

    model_config = ConfigDict(from_attributes=True)