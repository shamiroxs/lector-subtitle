import os
import shutil

def get_user_input():
    user_input = input("Enter the video file name (without .mp4): ").strip()
    return user_input + ".mp4"

def find_and_rename_file(user_input_file):
    # Source directory
    source_dir = "../../../sdcard/Movies/VLLO"
    
    # Destination directory
    destination_dir = "./input"
    destination_file = os.path.join(destination_dir, "video.mp4")

    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Full path to the source file
    source_file = os.path.join(source_dir, user_input_file)

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"File '{user_input_file}' does not exist in '{source_dir}'.")
        return

    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it.")
        os.makedirs(destination_dir)

    # Copy and rename the file
    try:
        shutil.copy2(source_file, destination_file)
        print(f"File renamed to 'video.mp4' and stored in '{destination_dir}'.")
    except Exception as e:
        print(f"Error while copying and renaming file: {e}")

if __name__ == "__main__":
    user_input_file = get_user_input()
    find_and_rename_file(user_input_file)
