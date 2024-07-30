import os
import sys
import yt_dlp
import util
from util import construct_video_path
from constants import *

# Download specific YouTube video of highest quality
def download_video(url, output_path):
    # Attempt to download file at URL
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
            'quiet': True,
            'no_warnings': True,
        }
        # Download youtube video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Downloaded: {os.path.basename(output_path)}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

# Download all 
def download_explanations(categories):
    base_dir = "nc150_videos"
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Record fails later to display to user if needed
    fail_count = 0
    for category_name, category in categories.items():
        # Create a directory for the category
        category_dir = os.path.join(base_dir, category_name)
        # Only create category if it does not exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        # Download Neetcode explanation video for each category problem
        for problem in category.problems:
            if problem.neetcode_url:
                output_path = construct_video_path(category, problem)

                # Check if video not already downloaded
                if not os.path.exists(output_path):
                    print(f"Downloading: {problem.problem_name}")
                    success = download_video(problem.neetcode_url, output_path)

                    if not success:
                        fail_count += 1
                        print(f"Failed to download {problem.problem_name}")
                else:
                    print(f"Skipped (already exists): {problem.problem_name}")
            # Skip problems with no Neetcode link
            else:
                print(f"Skipped (no URL): {problem.problem_name}")

    if fail_count == 0:
        print("Download process completed successfully.")
    else:
        print(f"{fail_count}/{TOTAL_PROBLEMS} failed downloads.")
