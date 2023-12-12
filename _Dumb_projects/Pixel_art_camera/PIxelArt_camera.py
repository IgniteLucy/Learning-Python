#special thanks to https://www.youtube.com/watch?v=FygLqV15TxQ&t - Nicholas Renotte
#Import opencv for computervision stuff
import cv2
# Importying matplotlib so we can visualize an image
from matplotlib import pyplot as plt
import os

#Get the main directory working space for this working script
script_dir = os.path.dirname(os.path.abspath(__file__))

#creawte directory for pictures if not existing
output_dir = os.path.join(script_dir, 'output_pictures')
os.makedirs(output_dir, exist_ok=True)


existing_files =  [f for f in os.listdir(output_dir) if f.endswith('.jpg')]

index = len(existing_files) + 1


# Construct the full path for the output image in the output_pictures directory
output_image_path = os.path.join(output_dir, f'output_image_{index}.jpg')



#Connect the webcam
cap = cv2.VideoCapture(0)
# Get a frame from the capture device
ret, frame = cap.read()


#Resize the frame 
#top qual -  width, height = 1560 , 1200
#Cursed qual - width, height = 52 , 40
width, height = 91 , 70
frame  = cv2.resize(frame, (width,height))


cv2.imshow("Resized Frame", frame)

cv2.imwrite(output_image_path,frame)

#Display the resized frame
#plt.imshow(frame)
#plt.show()

#Release the capture device
cap.release()
cv2.destroyAllWindows()

