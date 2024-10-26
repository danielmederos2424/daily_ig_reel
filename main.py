from instagrapi import Client
import schedule
import time
from datetime import datetime

def authenticate():
    print("Starting authentication...")
    try:
        client = Client()
        client.login("user", "password")
        print("Authentication successful.")
        return client
    except Exception as e:
        print(f"Authentication error: {e}")
        return None

# Function to get the current day count
def get_day_count():
    print("Retrieving current day count...")
    try:
        with open("day_counter.txt", "r") as file:
            day = int(file.read())
        print(f"Current day count is: {day}")
    except FileNotFoundError:
        day = 1
        print("No previous day count found. Starting at day 1.")
    return day

# Function to increment the day count
def increment_day_count():
    day = get_day_count() + 1
    with open("day_counter.txt", "w") as file:
        file.write(str(day))
    print(f"Day count incremented to: {day}")

# Function to upload the reel
def upload_reel():
    print("Starting reel upload process...")
    client = authenticate()
    if not client:
        print("Authentication failed. Upload canceled.")
        return

    video_path = "/path/to/video.mp4"
    day_count = get_day_count()
    caption = f"Day {day_count}"
    
    print(f"Uploading reel with caption: {caption}")
    try:
        client.video_upload(video_path, caption)
        print(f"Upload successful: Day {day_count}")
        increment_day_count()
    except Exception as e:
        print(f"Error uploading reel: {e}")

print("Scheduling daily upload at 10:00 AM...")
schedule.every().day.at("10:00").do(upload_reel)

print("Performing the first upload immediately...")
upload_reel()

# Run the waiting loop to check scheduled tasks
print("Starting main loop to check scheduled tasks.")
while True:
    print("Checking for scheduled tasks...")
    schedule.run_pending()
    print("No tasks to run at the moment. Sleeping for 1 hour.")
    time.sleep(3600)  # Check every hour
