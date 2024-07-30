import os

def construct_video_path(category, problem):
    base_dir = "neetcode_explanations"
    safe_filename = "".join([c for c in problem.problem_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    video_filename = f"{problem.difficulty}_{safe_filename}.mp4".lower().replace(" ", "_")
    return os.path.join(base_dir, category, video_filename)

# Open video file at video_path
def open_video(video_path):
    if os.name == 'nt':  # For Windows
        os.startfile(video_path)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.call(('open', video_path))
    else:
        print(f"Unsupported operating system. Please open the video manually: {video_path}")