import os
from progress_manager import save_progress

def construct_video_path(category, problem):
    base_dir = "nc150_videos"
    safe_filename = "".join([c for c in problem.problem_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    video_filename = f"{problem.difficulty}_{safe_filename}.mp4".lower().replace(" ", "_")
    return os.path.join(base_dir, category.category_name, video_filename)

# Open video file at video_path
def open_video(video_path):
    if os.name == 'nt':  # For Windows
        os.startfile(video_path)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.call(('open', video_path))
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
    if confirm.lower() == 'y':
        # Reset completition status for each problem
        for category in categories.values():
            for problem in category.problems:
                problem.is_completed = False
        save_progress(categories)
        print("All problem completion data has been reset.")
    else:
        print("Operation cancelled.")