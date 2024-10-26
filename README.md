# Daily Instagram Reel Uploader

This repository contains a script that automates the daily upload of Instagram reels using the `instagrapi` library. The script authenticates, uploads a video, and schedules the task to run daily at a specified time.

## Features

- **Authentication**: Logs in to Instagram using provided credentials.
- **Daily Counter**: Maintains a daily counter to track the number of uploads.
- **Video Upload**: Uploads a video to the Instagram feed with a caption indicating the day count.
- **Scheduling**: Schedules the upload task to run daily at 10:00 AM.

## Install dependencies**:
    ```sh
    pip install instagrapi schedule
    ```

## Usage

1. **Set your Instagram credentials**: Replace `"username"` and `"password"` in the `authenticate` function with your actual Instagram credentials.

2. **Prepare your video**: Place the video you want to upload in the specified path (`"path/to/your/video.mp4"`).

3. **Run the script**:
    ```sh
    python3 main.py
    ```


## Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.
