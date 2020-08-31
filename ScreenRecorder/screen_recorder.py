import cv2
import numpy as np
import pyautogui




class ScreedRecorder():

    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = pyautogui.size()
    frame_per_second = float(20.0)
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, frame_per_second, (SCREEN_SIZE))

    def __init__(self):
        self.is_started = False


    def Start(self):
        self.is_started =True

    def Stop(self):
        self.is_started = False

    while self.is_started:
        # make a screenshot
        img = pyautogui.screenshot()
        # img = pyautogui.screenshot(region=(0, 0, 300, 400))
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        cv2.imshow("screenshot", frame)
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()