import os
import whisper
from moviepy.editor import VideoFileClip
import json

# Step 1: Paths and File Handling
input_directory = "input"
input_video = os.path.join(input_directory, "video.mp4")
output_json = "subtitle.json"
max_duration = 2  # Maximum duration for each subtitle in seconds

# Step 2: Extract Audio from Video
def extract_audio(video_path, audio_output="audio.mp3"):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output, logger=None)
    video.close()
    audio.close()
    return audio_output

# Step 3: Transcribe Audio using Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["segments"]

# Step 4: Split Long Segments into Smaller Chunks
def split_segments(segments, max_duration):
    new_segments = []
    
    for segment in segments:
        start, end, text = segment["start"], segment["end"], segment["text"]
        duration = end - start

        if duration <= max_duration:
            # If the segment is already within the duration limit, add it directly
            new_segments.append(segment)
        else:
            # Split the segment into smaller chunks
            words = text.split()
            total_words = len(words)
            chunk_start = start
            chunk_text = []

            for i, word in enumerate(words):
                chunk_text.append(word)
                # Estimate duration for the current chunk
                avg_word_duration = duration / total_words
                chunk_end = chunk_start + avg_word_duration * len(chunk_text)

                # Finalize the chunk if it exceeds max_duration or is the last word
                if chunk_end - chunk_start >= max_duration or i == len(words) - 1:
                    new_segments.append({
                        "start": chunk_start,
                        "end": min(chunk_end, end),  # Ensure end does not exceed original segment
                        "text": " ".join(chunk_text),
                    })
                    chunk_start = chunk_end  # Update start for the next chunk
                    chunk_text = []  # Reset text for the new chunk

    return new_segments


# Step 5: Save Subtitles to JSON
def save_subtitle_json(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(segments, f, ensure_ascii=False, indent=4)

# Step 6: Main Process
def main():
    print("Extracting audio from video...")
    audio_path = extract_audio(input_video)

    print("Transcribing audio...")
    segments = transcribe_audio(audio_path)

    print("Splitting long segments...")
    segments = split_segments(segments, max_duration)

    print("Saving subtitles to JSON...")
    save_subtitle_json(segments, output_json)

    print(f"Subtitle JSON saved to {output_json}")

if __name__ == "__main__":
    main()

