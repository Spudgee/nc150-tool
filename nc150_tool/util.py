import os
import subprocess
import platform
from progress_manager import save_progress

# Construct appropriate, clean path for loading and saving videos
def construct_video_path(category, problem):
    base_dir = "nc150_videos"
    safe_filename = "".join([c for c in problem.problem_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    video_filename = f"{problem.difficulty}_{safe_filename}.mp4".lower().replace(" ", "_")
    
    # Obtain category name as string for path creation
    category_name = category if isinstance(category, str) else category.category_name
    return os.path.join(base_dir, category_name, video_filename)

# Open video file at video_path
def open_video(video_path):
    # Running Windows
    if platform.system() == "Windows":
        os.startfile(video_path)
    # Running Mac OS
    elif platform.system() == "Darwin":
        subprocess.call(('open', video_path))
    # Running Linux
    elif platform.system() == "Linux":
        try:
            subprocess.call(('xdg-open', video_path))
        except FileNotFoundError:
            try:
                subprocess.call(('gio', 'open', video_path))
            except FileNotFoundError:
                print(f"Could not open the video. Please open it manually: {video_path}")
    else:
        print(f"Unsupported operating system. Please open the video manually: {video_path}")

# Delete all local downloaded explanation videos
def delete_videos():
    video_dir = "nc150_videos"
    if os.path.exists(video_dir):
        shutil.rmtree(video_dir)

# Reset compleition status for all problems
def reset_completion_data(categories):
    confirm = input("Are you sure you want to reset problem completion data? (y/n): ")
    # Confirm deletion of all problem completion
    if confirm.lower() == 'y':
        # Reset completition status for each problem
        for category in categories.values():
            for problem in category.problems:
                problem.is_completed = False
        save_progress(categories)
        print("All problem completion data has been reset.")
    else:
        print("Operation cancelled.")