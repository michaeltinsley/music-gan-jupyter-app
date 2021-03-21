import uuid
from dataclasses import dataclass
from typing import Optional

from google.colab import files
from lucidsonicdreams import LucidSonicDream

from .music_download import download_youtube_mp3


@dataclass
class LucidDreamConfig:
    url: str
    style: str
    resolution: int
    speed_fpm: int
    start_time: int

    pulse_react: float
    pulse_percussive: bool
    pulse_harmonic: bool

    motion_react: float
    motion_percussive: bool
    motion_harmonic: bool

    class_pitch_react: float
    class_smooth_seconds: int
    class_complexity: float
    class_shuffle_seconds: int

    contrast_strength: float
    contrast_percussive: bool
    flash_strength: float
    flash_percussive: bool

    length: Optional[int] = None


class LucidDreamWrapper:
    def __init__(self, config: LucidDreamConfig) -> None:
        """"""
        self.config = config
        self.id = str(uuid.uuid4())
        self.video_name = f"{self.id}.mp4"

    def download_music(self) -> None:
        """
        Downloads the given track and saves the filepath.
        """
        saved_file = download_youtube_mp3(self.config.url, self.id)
        self.audio_track = saved_file

    def download_weights(self) -> None:
        """
        Downloads the model weights.
        """
        self.lucid_dream = LucidSonicDream(
            song=self.audio_track,
            style=self.config.style,
        )

    def generate(self) -> None:
        """
        Generate the output video.
        """
        self.lucid_dream.hallucinate(
            file_name=self.video_name,
        )

    def download(self) -> None:
        """
        Download the generated video from Colab.
        """
        files.download(self.video_name)
