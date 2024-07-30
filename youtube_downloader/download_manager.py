import os
import sys
from yt_dlp import YouTube

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output_path)
        print("Download completed!")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

def download_explanations(categories):