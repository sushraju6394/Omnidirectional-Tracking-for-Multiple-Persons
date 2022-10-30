from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2


def objectTracker(bbox):
# construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", type=str, help="path to input video file",default='try.mp4')
    ap.add_argument("-t", "--tracker", type=str, default="csrt", help="OpenCV object tracker type")
    args = vars(ap.parse_args())



# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations
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

    video_writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 20,(640,480))
    boxes = []
    count = 1
    
# loop over frames from the video stream
    while True:
	# grab the current frame, then handle if we are using a
	# VideoStream or VideoCapture object
        frame = vs.read()
        frame = frame[1] if args.get("video", False) else frame
 
	# check to see if we have reached the end of the stream
        if frame is None:
            break
 
	# resize the frame (so we can process it faster)
	#frame = imutils.resize(frame, width=600)

        # grab the updated bounding box coordinates (if any) for each
	# object that is being tracked
        if len(boxes)== 0:
            boxes = bbox
            for val in bbox:
                tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
                trackers.add(tracker, frame, tuple(val))
        else:
            (success, boxes) = trackers.update(frame)
 
	# loop over the bounding boxes and draw then on the frame
        #person_id = 1
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.putText(frame,person_id,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
            #person_id = person_id + 1
            
	# show the output frame
        video_writer.write(frame)
        print(count)
        count = count + 1
        key = cv2.waitKey(1) & 0xFF
 
	# if the 's' key is selected, we are going to "select" a bounding
	# box to track
        #if key == ord("s"):
	    # select the bounding box of the object we want to track (make
	    # sure you press ENTER or SPACE after selecting the ROI)
            #box = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
 
	    # create a new object tracker for the bounding box and add it
	    # to our multi-object tracker
            #tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
            #trackers.add(tracker, frame, box)



	# if the `q` key was pressed, break from the loop
        #elif key == ord("q"):
            #break
 
    # if we are using a webcam, release the pointer
    if not args.get("video", False):
        vs.stop()
    # otherwise, release the file pointer
    else:
        vs.release()

    video_writer.release()
