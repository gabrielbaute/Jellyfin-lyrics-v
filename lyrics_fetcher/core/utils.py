import logging
import os
from tinytag import TinyTag

def get_song_details(file_path: str):
    """Extract params from audio file"""
    try:
        audio = TinyTag.get(file_path)
        return audio.album, audio.title, audio.artist, int(audio.duration)
    except Exception as e:
        logging.error(f"Error extracting details from {file_path}: {e}")
        return None, None, None, None

def collect_audio_files(directory_path: str):
    """Collects audio file in directory"""
    try:
        audio_files = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith(('.flac', '.mp3', '.wav', '.ogg', '.aac', '.wma')):
                    audio_files.append(os.path.join(root, file))
        return audio_files
    except Exception as e:
        logging.error(f"Error collecting audio files: {e}")
        return []

def replaces(directory):
    """For windows enviroments. Replaces "\\" with "/"
    """
    folder_path = directory.replace("\\","/")
    return folder_path