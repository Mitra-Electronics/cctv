import cv2
from json import load as json_load
from pathlib import Path
import threading
from skvideo.io import FFmpegWriter
import socket
import numpy as np

record = True

file_path = Path(__file__).parent

def camera_handle(source, filename, url):
    video = cv2.VideoCapture(source)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 12395
    sock.connect((HOST, PORT))
    video_rec = FFmpegWriter(filename,{"-pix_fmt":"bgr24"}, {"-q":"0"})

    while video.isOpened():
        # get the frame from the webcam
        stream_ok, frame = video.read()
        
        # display current frame
        frame = cv2.flip(frame, 1)
            
        # write frame to the video file
        if record == True:
            video_rec.writeFrame(frame)
        else:
            video_rec.close()

        ret, jpeg = cv2.imencode('.jpg', frame)
        data_encode = np.array(jpeg.tobytes())
        str_encode = data_encode.tostring()
        sock.send(str_encode)


    # clean ups
    cv2.destroyAllWindows()
    sock.close()

    # release web camera stream
    video.release()
    video_rec.close()

if __name__ == '__main__':
    file_obj = open(file_path / "config.json", "r")
    json_file = json_load(file_obj)
    file_obj.close()
    for camera in json_file["cameras"]:
        process = threading.Thread(target=camera_handle, args=(camera["source"], camera["file_name"], camera["streaming_url"]))
        process.start()

