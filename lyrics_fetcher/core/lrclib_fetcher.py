import logging
import requests
from typing import Optional, Dict, Any

class LRCLibClient:
    """A client to fetch lyrics from the LRCLib API."""

    def __init__(self, api_url: str = "https://lrclib.net/api/get", timeout: int = 10):
        """
        Initialize the LRCLib client.
        
        Args:
            api_url (str): Base URL of the LRCLib API.
            timeout (int): Timeout in seconds for API requests.
        """
        self.api_url = api_url
        self.timeout = timeout
        self.session = requests.Session()  # Reutiliza conexiones HTTP

    def get_lyrics(
        self,
        artist: str,
        title: str,
        album: str,
        duration: int,
        fallback_to_plain: bool = True
    ) -> Optional[str]:
        """
        Fetch lyrics (synced or plain) from LRCLib.
        
        Args:
            artist: Artist name.
            title: Song title.
            album: Album name.
            duration: Song duration in seconds.
            fallback_to_plain: If True, falls back to plain lyrics if synced lyrics are not found.
        
        Returns:
            str: Lyrics (synced or plain), or None if not found.
        """
        params: Dict[str, Any] = {
            "artist_name": artist,
            "track_name": title,
            "album_name": album,
            "duration": duration,
        }

        try:
            response = self.session.get(
                self.api_url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()  # Lanza excepción para códigos 4XX/5XX

            data = response.json()
            lyrics = data.get("syncedLyrics")

            if lyrics is None and fallback_to_plain:
                logging.info(f"Synced lyrics not found for '{title}'. Falling back to plain lyrics.")
                lyrics = data.get("plainLyrics")

            return lyrics

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching lyrics for '{title}': {e}")
            return None