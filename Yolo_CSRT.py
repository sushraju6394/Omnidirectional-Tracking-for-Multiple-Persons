from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
from darkflow.net.build import TFNet
import numpy as np

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.9}
tfnet = TFNet(options)
person_bbox = []
boxes = []
count = 1

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
	help="path to input video file",default='try.mp4')
ap.add_argument("-t", "--tracker", type=str, default="csrt",
	help="OpenCV object tracker type")
args = vars(ap.parse_args())



OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}
 
# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()

# if a video path was not supplied, grab the reference to the web cam
if not args.get("video", False):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(1.0)
 
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])

# loop over frames from the video stream
while True:
	
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
 	if frame is None:
		break
 	frame = imutils.resize(frame, width=600)
    result = tfnet.return_predict(frame)
        person_pred = []
        for val in result: 
            if val['label'] == 'person':
                person_pred.append([val['topleft']['x'], val['topleft']['y'], val['bottomright']['x'] - val['topleft']['x'], val['bottomright']['y'] - val['topleft']['y']])
                person_bbox.append(person_pred)
                print(person_bbox[0])
                
    if len(boxes)== 0:
        boxes = person_bbox[0]
        for val in person_bbox[0]:
        tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
        trackers.add(tracker, frame, tuple(val))
    else:    
        (success, boxes) = trackers.update(frame)
        
    person_id = 1  
	for box in boxes:
		(x, y, w, h) = [int(v) for v in box]
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame,person_id,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        person_id = person_id + 1
        
    cv2.imwrite('/home/sushmitha/darkflow/output_images.png',frame)    
    video_writer.write(frame)
    print(count)
    count = count + 1
    key = cv2.waitKey(1) & 0xFF
    
video_writer = cv2.VideoWriter("result_video.avi", cv2.VideoWriter_fourcc(*"MJPG"), 20,(640,480))		
if not args.get("video", False):
	vs.stop()
 
else:
	vs.release()
 
cv2.destroyAllWindows()
