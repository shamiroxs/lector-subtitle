#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip
from tqdm import tqdm

# Environment variable to avoid ImageMagick usage
os.environ["TEXTCLIP_USE_IMAGEMAGICK"] = "False"

def burn_subtitles(video_path, subtitle_path, output_dir):
    """
    Burn subtitles into the video.
    
    Args:
        video_path (str): Path to the input video.
        subtitle_path (str): Path to the subtitle JSON file.
        output_dir (str): Directory to save the output video.
    """
    # Load subtitles from JSON
    with open(subtitle_path, "r") as f:
        subtitles = json.load(f)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "output_video.mp4")

    # Open video file
    video = VideoFileClip(video_path)

    # Settings
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_size = 24
    bottom_space = 50

    # Prepare captions for rendering
    caption_data = [
        {
            "text": sub["text"],
            "start": sub["start"],
            "end": sub["end"],
        }
        for sub in subtitles
    ]

    def render_frame(get_frame, t):
        """
        Render subtitles on a video frame.

        Args:
            get_frame (function): Function to get the current frame.
            t (float): Current timestamp.
        """
        frame = get_frame(t)
        current_caption = next(
            (c for c in caption_data if c["start"] <= t <= c["end"]), None
        )

        if current_caption:
            image = Image.fromarray(frame)
            draw = ImageDraw.Draw(image)

            # Load font
            font = ImageFont.truetype(font_path, font_size)

            # Measure text dimensions
            text_bbox = draw.textbbox((0, 0), current_caption["text"], font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            # Position the text at the bottom center
            w, h = frame.shape[1], frame.shape[0]
            text_x = w // 2 - text_width // 2
            text_y = h // 2 - text_height // 2 + 80
            pos = (text_x, text_y)
            
             # Draw background rectangle
            padding = 15  # Padding around the text
            box = [
                text_x - padding,
                text_y - padding,
                text_x + text_width + padding,
                text_y + text_height + padding,
            ]
            draw.rectangle(box, fill=(0, 0, 0, 200))  # Semi-transparent black box
            #draw.rectangle(box, fill=(34, 45, 40, 255))  # Opaque dark gray-green box
            #draw.rectangle(box, fill=(255, 255, 0, 255))  # Opaque yellow box
            
            # Draw text with stroke
            draw.text(
                pos,
                current_caption["text"],
                fill="white",
                font=font,
                stroke_width=2,
                stroke_fill="black",
                align="center",
            )

            return np.array(image)

        return frame

    # Process video frames
    print(f"Starting subtitle burn-in process. Output will be saved to {output_path}.")
    processed_video = video.fl(lambda gf, t: render_frame(gf, t))
    
    # Save the output video
    processed_video.write_videofile(output_path, codec="libx264", fps=video.fps)
    print("Subtitle burn-in completed successfully.")

if __name__ == "__main__":
    video_path = "./input/video.mp4"
    subtitle_path = "./subtitle.json"
    output_dir = "./output"

    # Call the burn_subtitles function
    burn_subtitles(video_path, subtitle_path, output_dir)
