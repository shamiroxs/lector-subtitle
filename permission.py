import os

# Define the path to the video file
video_file = './output/output_video.mp4'

# Function to change file permissions
def set_video_permissions(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Change permissions to 644 (rw-r--r--)
            os.chmod(file_path, 0o644)
            print(f"Permissions for {file_path} set to 644 (rw-r--r--)")
        else:
            print(f"Error: {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function to set permissions
set_video_permissions(video_file)

