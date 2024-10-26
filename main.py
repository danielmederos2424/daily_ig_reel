from instagrapi import Client
import schedule
import time
from datetime import datetime

def authenticate():
    try:
        client = Client()
        client.login("username", "password")
        return client
    except Exception as e:
        print(f"Authentication error: {e}")
        return None

# Function to get the current day count
def get_day_count():
    try:
        with open("day_counter.txt", "r") as file:
            day = int(file.read())
    except FileNotFoundError:
        day = 1
    return day


def increment_day_count():
    day = get_day_count() + 1
    with open("day_counter.txt", "w") as file:
        file.write(str(day))


def upload_reel():
    client = authenticate()
    if not client:
        print("Authentication failed. Upload canceled.")
        return

    video_path = "path/to/your/video.mp4"
    day_count = get_day_count()
    caption = f"Day {day_count} \n "

    try:
        client.video_upload_to_feed(video_path, caption)
        print(f"Upload successfull: Day {day_count}")
        increment_day_count()
    except Exception as e:
        print(f"Error uploading: {e}")

# Schedule the daily task at 10:00 AM
schedule.every().day.at("10:00").do(upload_reel)

# Run the waiting loop to check scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(3600)  # Check every hour
