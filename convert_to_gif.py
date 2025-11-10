from moviepy.video.io.VideoFileClip import VideoFileClip

# Load your MP4
clip = VideoFileClip("videos/streamlit_demo.mp4")

# Trim if you want, make sure end time <= clip.duration
clip = clip.subclipped(0, min(6, clip.duration))  # first 6 seconds or full video

# Convert to GIF
clip.write_gif("videos/streamlit_demo.gif", fps=10)


# Convert to GIF
clip.write_gif("videos/streamlit_demo.gif", fps=10)
