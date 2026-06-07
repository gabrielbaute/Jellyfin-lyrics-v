from typing import Optional
from pydantic import BaseModel, ConfigDict

class LyricsResponseModel(BaseModel):
    """
    Data model for the response from LRCLib API when fetching lyrics.

    Attributes:
        id (Optional[int]): Unique identifier for the track in LRCLib.
        trackName (Optional[str]): Name of the track.
        artistName (Optional[str]): Name of the artist.
        albumName (Optional[str]): Name of the album.
        duration (Optional[int]): Duration of the track in seconds.
        instrumental (Optional[bool]): Whether the track is instrumental or not.
        plainLyrics (Optional[str]): Plain text lyrics of the track.
        syncedLyrics (Optional[str]): Synchronized lyrics with timestamps.
    """
    id: Optional[int] = None
    trackName: Optional[str] = None
    artistName: Optional[str] = None
    albumName: Optional[str] = None
    duration: Optional[int] = None
    instrumental: Optional[bool] = None
    plainLyrics: Optional[str] = None
    syncedLyrics: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)