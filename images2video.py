import cv2
import os
from imutils.video import VideoStream
import argparse
import imutils
import time

image_folder = 'G:\PYTHON CODES RP\output_images_csrt\images%03d.jpg'
video_name = 'csrt.avi'

images = [images for images in os.listdir(image_folder) if images.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
    
cv2.destroyAllWindows()
video.release()
