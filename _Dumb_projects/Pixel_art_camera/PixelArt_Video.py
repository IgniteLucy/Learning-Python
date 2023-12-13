import os
import cv2

#Get the main directory working space for this working script
script_dir = os.path.dirname(os.path.abspath(__file__))

#creawte directory for videos if not existing
output_dir = os.path.join(script_dir, 'output_videos')
os.makedirs(output_dir, exist_ok=True)

#Get exisiting files in the directory 

existing_files = [f for f in os.listdir(output_dir) if f.endswith('.mp4')]

#Calculate the index for the new video file
index = len(existing_files) + 1


# Construct the full path for the output video in the output_videos directory

output_video_path = os.path.join(output_dir,f'output_video_{index}.mp4')

# 0 should standard camera if not cycle through it
cap = cv2.VideoCapture(0)

frame_width =  int(cap.get(3))
frame_height = int(cap.get(4))

#Adjusted frame rate
frame_rate = 5 # 5 frames taken per second
capture_interval = int(cap.get(cv2.CAP_PROP_FPS)/ frame_rate)

#Custom directory
#output_video_path = os.path.join(output_dir, 'output_video.mp4')


video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))


for i in range(15):    #capture 15 frames
    ret, frame = cap.read()

    if not ret:
        break

    #write the frame to the video file
    video_writer.write(frame)

    #Display the frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(capture_interval) & 0xFF == 27:
        break
#Release sources
cap.release()
video_writer.release()
cv2.destroyAllWindows()