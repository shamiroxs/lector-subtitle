# lector-subtitle

A versatile utility to burn subtitles into videos. This tool is optimized for both general systems and Termux platforms, with additional scripts for managing file permissions and storage on Termux.

This project is an extension of the main [lector](https://github.com/shamiroxs/lector) project, which converts ebooks into audiobook videos.

## Video demo
[![Watch this YouTube Short](https://img.youtube.com/vi/ERSAfOMdn-E/maxresdefault.jpg)](https://youtube.com/shorts/ERSAfOMdn-E?si=VqcBMS3uOLHypjvj)

## Features

- **Subtitle Burning**: Burn `.json` subtitles into video files.
- **Audio Merging**: Add external audio tracks to subtitled videos.
- **Termux Support**: Includes helper scripts for file handling and permissions in Termux.
- **Customizable Subtitles**: Adjust font, positioning, background, and style.
- **Automated Workflow**: Use `run.py` to handle the full process seamlessly.

## Requirements

### General Requirements
- Python 3.8 or higher
- Recommended: Virtual environment for Python dependencies

### Python Dependencies:
- `moviepy`
- `Pillow`
- `numpy`
- `tqdm`

Install dependencies:
```bash
pip install -r requirements.txt
```

### Termux-Specific Requirements
For users on Termux, ensure the following:
- **Storage Permission**: Run `termux-setup-storage` before executing any script.
- Enable storage read/write permissions by running the `permission.py` script (optional).

## Installation

Clone the repository:
```bash
git clone https://github.com/shamiroxs/lector-subtitle.git
cd lector-subtitle
```

## Usage

### General Usage

#### Step 1: Burn Subtitles
1. Prepare a `.json` subtitle file with this structure:
   ```json
   [
       { "start": 0.0, "end": 2.0, "text": "Subtitle Text 1" },
       { "start": 2.0, "end": 4.0, "text": "Subtitle Text 2" }
   ]
   ```

2. Use `integrate.py` to burn subtitles into the video:
   ```bash
   python integrate.py
   ```

   Default paths:
   - Video: `./input/video.mp4`
   - Subtitles: `./subtitle.json`
   - Output: Saved in `./output/output_video.mp4`

#### Step 2: Merge Audio (Optional)
If your video has no audio, place an `audio.wav` file in the current directory, and the script will automatically merge it with the video.

#### Step 3: Automate Everything
Run `run.py` to combine burning subtitles and merging audio:
```bash
python run.py
```

### Termux-Specific Scripts

For Termux users, additional scripts are available:

- **permission.py**: Grants necessary storage permissions in Termux.
- **open.py**: Opens the output video using the default video player.
- **save.py**: Moves the final video to a specific location (e.g., external storage).

These scripts are commented out by default. To enable them:
1. Open the respective `.py` file.
2. Uncomment the execution lines to enable the functionality.
3. Run the script using:
   ```bash
   python <script_name>.py
   ```

Example:
```bash
python permission.py  # Grants Termux storage permissions
python open.py         # Opens the output video
python save.py         # Saves the video to external storage
```

### File Locations

- **Input Video**: Place the video in the `./input/` directory as `video.mp4`.
- **Subtitles**: Create a `subtitle.json` file in the project root.
- **Output Video**: Generated in the `./output/` directory as `output_video.mp4`.

## Development Notes

- Default font: **DejaVu Sans Bold**. Modify the font and styles in `integrate.py` as needed.
- Customize subtitle background, position, and colors directly in the code.

## Contributing

Contributions to improve Termux integration or extend functionality are welcome. Fork this repository, make changes, and submit a pull request.

## Main Project

This tool is part of the **lector** ecosystem. Learn more about the main project here:  
[lector: Convert ebooks to audiobook videos](https://github.com/shamiroxs/lector)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
