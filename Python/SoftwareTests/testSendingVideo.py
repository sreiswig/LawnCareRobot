import sys
import cv2
import json

def read_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    return config

#Set gstreamer pipeline parameters
def gstreamer_pipeline(
    capture_width=1280, #Camera pre-captured image width
    capture_height=720, #Camera pre-captured image height
    display_width=1280, #Window display image width
    display_height=720, #Window display image height
    framerate=60,       #Capture frame rate
    flip_method=0,      #Whether to rotate the image
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def read_cam():
    config = read_config()
    capture_width = 1280
    capture_height = 720
    display_width = 1280
    display_height = 720
    framerate = 60
    flip_method = 0

    # Create pipeline
    print(gstreamer_pipeline(capture_width,capture_height,display_width,display_height,framerate,flip_method))

    #Pipeline and video stream binding
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('Src opened, %dx%d @ %d fps' % (w, h, fps))
    print(cv2.CAP_GSTREAMER)

    gst_out = f"appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! x264enc ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host={config['mqtt']['host']} port=1234 "
    out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, float(fps), (int(w), int(h)))
    if not out.isOpened():
        print("Failed to open output")
        exit()

    if cap.isOpened():
        while True:
            ret_val, img = cap.read()
            height, width = img.shape[0:2]
            print("Image Values: ")
            print(img)
            print("Ret Val")
            print(ret_val)

            if width > 800:
                new_width = 640
                new_height = int(new_width/width*height)
                img = cv2.resize(img, (new_width, new_height))

            if not ret_val:
                break
            out.write(img)
            keyCode = cv2.waitKey(30) & 0xFF         
            if keyCode == 27:# ESC key to exit
                break

    else:
        print("pipeline open failed")

    print("successfully exit")
    cap.release()
    out.release()


if __name__ == '__main__':
    read_cam()