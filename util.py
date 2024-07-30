import os

def construct_video_path(category, problem):
    base_dir = "neetcode_explanations"
    safe_filename = "".join([c for c in problem.problem_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
    video_filename = f"{problem.difficulty}_{safe_filename}.mp4".lower().replace(" ", "_")
    return os.path.join(base_dir, category, video_filename)