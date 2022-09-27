import test_utils
import requests
import cv2 as cv
from PIL import Image

def test():
    api_json = test_utils.read_app_config()
    config_json = test_utils.read_config()
    capture_width = 1280
    capture_height = 720
    display_width = 1280
    display_height = 720
    framerate = 60
    flip_method = 0

    # Create pipeline
    print(test_utils.gstreamer_pipeline(capture_width,capture_height,display_width,display_height,framerate,flip_method))

    #Pipeline and video stream binding
    cap = cv.VideoCapture(test_utils.gstreamer_pipeline(flip_method=0), cv.CAP_GSTREAMER)

    if cap.isOpened():
        ret_val, img = cap.read()
        # Failed to grab an image
        if not ret_val:
            print("failed to grab frame")
            return
        im = Image.fromarray(img)
        print(type(im))

        files = {'file': im}
        response = requests.post(api_json['url'], headers=api_json['headers'], files=files)
        print(response.json())
    else:
        print("Failed to open the camera")

    return

if __name__ == '__main__':
    test()