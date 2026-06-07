from lyrics_fetcher.errors.base_error import LyricsFetcherError

class APIError(LyricsFetcherError):
    """Communication error with an external API."""
    pass

class ValidationError(LyricsFetcherError):
    """Validation error for data or type."""
    pass

class ResourceNotFoundError(LyricsFetcherError):
    """When a resource (a Track, Album, etc.) does not exist."""
    pass

class LyricsNotFoundError(ResourceNotFoundError):
    """When no lyrics are found for a track."""
    pass

class StorageError(LyricsFetcherError):
    """Physical disk or quota errors."""
    pass

class PermissionDeniedError(LyricsFetcherError):
    """When no permissions are available to perform an action."""
    pass