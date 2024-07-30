import os
import sys
import yt_dlp

# Download specific YouTube video
def download_video(url, output_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
            'quiet': True,
            'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Downloaded: {os.path.basename(output_path)}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False


def download_explanations(categories):
    base_dir = "neetcode_explanations"
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for category_name, category in categories.items():
        # Create a directory for the category
        category_dir = os.path.join(base_dir, category_name)
        # Only create category if it does not exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        # Download Neetcode explanation video for each category problem
        for problem in category.problems:
            if problem.neetcode_url:
                # Create a safe filename 
                safe_filename = "".join([c for c in problem.problem_name if c.isalnum() or c in (' ', '-', '_')]).rstrip()
                # Convert to all lower case, replace spaces with underscores
                video_filename = f"{problem.difficulty}_{safe_filename}.mp4".lower().replace(" ", "_")
                output_path = os.path.join(category_dir, video_filename)

                # Check if video not already downloaded
                if not os.path.exists(output_path):
                    print(f"Downloading: {problem.problem_name}")
                    success = download_video(problem.neetcode_url, output_path)

                    if not success:
                        print(f"Failed to download {problem.problem_name}")
                else:
                    print(f"Skipped (already exists): {problem.problem_name}")
            # Skip problems with no Neetcode link
            else:
                print(f"Skipped (no URL): {problem.problem_name}")

    print("Download process completed.")
