"""
Helper functions for donwloading music from YouTube.
"""
import os
import uuid
from typing import Optional

import moviepy.editor as mp
from pytube import YouTube


def download_youtube_mp3(url: str, save_path: Optional[str] = "./tmp/") -> str:
    """
    Downloads a given YouTube video to MP3.

    :param url: The URL of the input video
    :param save_path: Output path
    :return: The filepath of the downloaded file.
    """
    video = YouTube(url)
    video = video.streams.filter(only_audio=True).first()
    _id = str(uuid.uuid4())
    video.download(output_path=save_path, filename=_id)
    video_path = f"{save_path}{_id}.mp4"
    clip = mp.AudioFileClip()
    audio_path = f"{save_path}{_id}.mp3"
    clip.write_audiofile(f"{save_path}{_id}.mp3")
    os.remove(video_path)
    return audio_path
