# FFmpeg Video Processing Internship Tasks

## 📌 Task 1: Extract Frames
- Extracted images from a YouTube video using FFmpeg
- Command used:
  ffmpeg -i video.mp4 -vf fps=1 image_%04d.jpg

## 📌 Task 2: Reconstruct Video
- Generated ~1800 frames (30 fps × 60 sec)
- Recreated video from frames
- Command used:
  ffmpeg -framerate 30 -i frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4

## 📌 Task 3: Add Audio
- Downloaded audio from Pixabay
- Trimmed audio to 1 minute
- Merged audio with video

Command used:
ffmpeg -i output.mp4 -i trimmed_audio.mp3 -c:v copy -c:a aac -shortest final_video.mp4

## 🛠 Tools Used
- FFmpeg
- Pixabay Music

## 🎥 Final Output
Final video with audio added

## 📂 Files Included
- output.mp4
- final_video.mp4
- sample images
