import cv2
import numpy as np
import pyautogui
import time

# Define screen resolution and frame rate
screen_size = pyautogui.size()
frame_rate = 20.0  #we can change this value based on our requirements

# Initialize the video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording.avi"
out = cv2.VideoWriter(output_file, fourcc, frame_rate, (screen_size.width, screen_size.height))

print("Recording started. Press Ctrl+C to stop.")

try:
    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a NumPy array
        frame = np.array(screenshot)

        # Convert the frame from RGB to BGR (required by OpenCV)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Wait to maintain the desired frame rate
        time.sleep(1 / frame_rate)

except KeyboardInterrupt:
    print("Recording stopped by user.")

# Release the video writer object
out.release()
print(f"Video saved as {output_file}")
