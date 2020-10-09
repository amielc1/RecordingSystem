import cv2
import numpy as np
import pyautogui


class ScreenRecorderConfig():

    def __init__(self, screen_size, frame_per_second, filename, codec):
        self.screen_size = screen_size
        self.frame_per_second = frame_per_second
        self.filename = filename
        self.codec = codec




class ScreedRecorder():
    # display screen resolution, get it from your OS settings
    screen_size = pyautogui.size()
    frame_per_second = float(20.0)
    filename = "output.avi"
    codec = "XVID"

    def __init__(self, screen_recorder_config):
        self.is_started = False
        self.codec = cv2.VideoWriter_fourcc(*screen_recorder_config.codec)
        self.out = cv2.VideoWriter(screen_recorder_config.filename, self.codec, screen_recorder_config.frame_per_second,
                                   screen_recorder_config.screen_size)

    # TODO: work on event start and stop record
    def record(self):
        while self.is_started:
            # make a screenshot
            img = pyautogui.screenshot()
            # img = pyautogui.screenshot(region=(0, 0, 300, 400))
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            self.out.write(frame)
            # # show the frame
            # cv2.imshow("screenshot", frame)
            # # if the user clicks q, it exits
            # if cv2.waitKey(1) == ord("q"):
            #     break
        # make sure everything is closed when exited
        cv2.destroyAllWindows()
        self.out.release()

    def Start(self):
        self.is_started = True
        self.record()

    def Stop(self):
        self.is_started = False


screen_size = pyautogui.size()
frame_per_second = float(20.0)
filename = "output.avi"
codec = "XVID"
screen_config = ScreenRecorderConfig(screen_size, frame_per_second, filename, codec)
screen_recorder = ScreedRecorder(screen_config)
screen_recorder.Start()
screen_recorder.Stop()
