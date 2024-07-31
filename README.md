# nc150-downloader
Download Neetcode 150 video explanations into organized folders according to the roadmap. Provide menu system for tracking the completion of different problems within the Neetcode 150 problem set. 

## Prerequisites
- Python 3.11.5
- `pip`

## Dependencies
- `yt-dlp`

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/spudgee/nc150-downloader.git
    cd nc150-downloader
    ```
2. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Run the script**:
    ```sh
    python main.py
    ```

## Usage
The program features a menu-driven interface. Navigate through the options by typing the appropriate number.

### Main Menu
1. **Download Manager**: Download NeetCode 150 explanation videos.
2. **Problem Manager**: View and manage your progress on NeetCode 150 problems within each category.
3. **Settings**: Manage user data and progress
4. **Exit**: Close the program.

### Download Manager
- Download NeetCode explanations: This will download video explanations for all problems in the NeetCode 150 list.

### Problem Manager
- View problems by category
- Mark problems as complete/incomplete
- Track your overall progress

### Settings
- Delete all downloaded videos
- Reset all problem completion data

## Features
- Organizes downloaded videos into category-specific folders
- Tracks problem completion status
- Provides a user-friendly interface for managing your NeetCode 150 progress
- Allows bulk downloading of video explanations

## File Structure
- `main.py`: Entry point of the program
- `menu.py`: Contains menu-related functions
- `downloader.py`: Handles video downloading functionality
- `category_initializer.py`: Initializes all category data
- `problem_initializer.py`: Initializes all problem data
- `util.py`: Contains utility functions
- `models.py`: Defines data models for categories and problems
- `constants.py`: Contains constants used within the program
- `/nc150_videos`: Contains downloaded videos organised within categories

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/your-username/nc150-downloader/issues) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [NeetCode](https://neetcode.io/) for providing the coding interview preparation material.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the video downloading functionality.
