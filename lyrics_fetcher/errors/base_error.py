from typing import Any, Dict, Optional

class LyricsFetcherError(Exception):
    """
    Base class for handling errors that are readable by humans.
    """
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}