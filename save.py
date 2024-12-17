import os
import shutil
from datetime import datetime

def rename_and_copy_file():
    # Source file path
    source_file = "./output/output_video.mp4"

    # Destination directory
    destination_dir = "../../../sdcard/shorts"

    # Ensure the source file exists
    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it.")
        os.makedirs(destination_dir)

    # Generate the new filename with current timestamp
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"vid{current_time}.mp4"

    # Full path for the new file
    destination_file = os.path.join(destination_dir, new_filename)

    # Copy and rename the file
    try:
        shutil.copy2(source_file, destination_file)
        print(f"File renamed and copied to: {destination_file}")
    except Exception as e:
        print(f"Error while copying file: {e}")

if __name__ == "__main__":
    rename_and_copy_file()

