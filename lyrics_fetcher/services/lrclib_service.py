"""LRC Lib API Client."""
import logging
from requests import Session, exceptions

from lyrics_fetcher.models import TrackModel, LyricsResponseModel
from lyrics_fetcher.errors import APIError, LyricsNotFoundError


class LyricService:
    """
    API Client for LRCLib to fetch song lyrics based on track information.

    Attributes:
        BASE_URL (str): Base URL for the LRCLib API.
        session (Session): Requests session for making API calls.
        logger (logging.Logger): Logger for logging messages.
    """
    
    BASE_URL: str = "https://lrclib.net/api"

    def __init__(self):
        """
        Initializes the LRCLib API service.

        Args:
            settings (AppSettings): Application configuration.
        """
        self.session = Session()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.session.timeout = 10

    def get_lyrics(self, track: TrackModel) -> LyricsResponseModel:
        """
        Fetches the synchronized or plain lyrics for a specific track.

        Args:
            track (TrackModel): Track object containing title, artist, album, and duration information.

        Returns:
            LyricsResponseModel: The lyrics response model if found, None otherwise.
        
        Raises:
            LyricsNotFoundError: If no lyrics are found for the given track.
            APIError: If there is an error connecting to the LRCLib API or fetching lyrics.
        """
        try:
            params = {
                "track_name": track.title,
                "artist_name": track.artists[0],
                "album_name": track.album,
                "duration": int(track.duration_seconds),
            }

            response = self.session.get(
                f"{self.BASE_URL}/get",
                params=params,
                headers={"Accept": "application/json"},
            )

            if response.status_code == 404:
                self.logger.warning(f"Lyrics not found for: {track.title} by {track.artists[0]}")
                raise LyricsNotFoundError(
                    message="Lyrics not found.",
                    details=f"Track: {track.title}, Artist: {track.artists[0]}"
                )

            response.raise_for_status()
            data = response.json()
            if not data:
                self.logger.warning(f"No lyrics data returned for: {track.title} by {track.artists[0]}")
                raise LyricsNotFoundError(
                    message="Lyrics not found.",
                    details=f"Track: {track.title}, Artist: {track.artists[0]}"
                )
            return LyricsResponseModel(**data)


        except exceptions.RequestException as e:
            self.logger.error(f"Error connecting to LRCLib API: {str(e)}")
            raise APIError(
                message="Error connecting to LRCLib API.",
                details=str(e),
            )
        except Exception as e:
            self.logger.error(f"Error fetching lyrics: {str(e)}")
            raise APIError(
                message="Error fetching lyrics.",
                details=str(e),
            )