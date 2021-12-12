import cv2
import skvideo.io

# open the webcam video stream
webcam = cv2.VideoCapture(0)

# open output video file stream
video = skvideo.io.FFmpegWriter("video.avi",{}, {"-q":"0", "-color_primaries": "3", "-color_trc": "1", "-colorspace": "1"})

# main loop
while True:
    # get the frame from the webcam
    stream_ok, frame = webcam.read()
    
    # if webcam stream is ok
    if stream_ok:
        # display current frame
        cv2.imshow('Webcam', frame)
        
        # write frame to the video file
        video.writeFrame(frame)

    # escape condition on Esc key pressed
    if cv2.waitKey(1) & 0xFF == 27: 
        break

# clean ups
cv2.destroyAllWindows()

# release web camera stream
webcam.release()

# release video output file stream
video.close()
