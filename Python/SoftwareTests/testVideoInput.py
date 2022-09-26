
import cv2 as cv
import numpy as np
import test_utils

if __name__ == "__main__":
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
        window_handle = cv.namedWindow("CSI Camera", cv.WINDOW_AUTOSIZE)
        
        # Frame by frame
        while cv.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
          # The image is too big to be adjusted
            height, width = img.shape[0:2]
            print("height=",height,"width=",width)
            if width > 800:
                new_width = 640
                new_height = int(new_width/width*height)
                img = cv.resize(img, (new_width, new_height))
            print("new_height=",new_height,"new_width=",new_width)

            cv.imshow("CSI Camera", img)
            #print("img.shape=",img.shape)
            keyCode = cv.waitKey(30) & 0xFF         
            if keyCode == 27:# ESC key to exit
                break
        #print("img.shape=",img.shape)
        #Release resources
        cap.release()
        cv.destroyAllWindows()
    else:
        print("Failed to open the camera")
