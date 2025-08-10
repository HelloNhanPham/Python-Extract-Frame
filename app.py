import streamlit as st
import cv2
import os

def extract_frames(video_path, start_frame, end_frame):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    extracted_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if start_frame <= frame_count <= end_frame:
            extracted_frames.append(frame)
        frame_count += 1

    cap.release()
    return extracted_frames

# Upload video file, only with mp4
video_file = st.file_uploader("Upload Video", type=["mp4"])
if video_file is not None:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_file.read())
    st.success("Video uploaded successfully!")

start_frame = st.number_input("Start Frame", min_value=0, value=0)
end_frame = st.number_input("End Frame", min_value=0, value=100)

if st.button("Extract Frames"):
    if start_frame >= end_frame:
        st.error("Start frame must be less than end frame.")
    else:
        extracted_frames = extract_frames("uploaded_video.mp4", start_frame, end_frame)
        os.remove("uploaded_video.mp4")
        st.success(f"Extracted {len(extracted_frames)} frames.")
        for i, frame in enumerate(extracted_frames):
            st.image(frame, caption=f"Frame {start_frame + i}")