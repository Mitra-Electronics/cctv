import cv2
from skvideo.io import FFmpegWriter

video = cv2.VideoCapture(0)
video_rec = FFmpegWriter("video.avi",{}, {"-q":"0", "-color_primaries": "3", "-color_trc": "1", "-colorspace": "1"})

while video.isOpened():
    # get the frame from the webcam
    stream_ok, frame = video.read()
    
    # if webcam stream is ok
    # display current frame
    frame = cv2.flip(frame, 1)
    cv2.imshow('CCTV', frame)
        
    # write frame to the video file
    video_rec.writeFrame(frame)

    # escape condition
    if cv2.waitKey(1) & 0xFF == 27: 
        break

# clean ups
cv2.destroyAllWindows()

# release web camera stream
video.release()
video_rec.close()