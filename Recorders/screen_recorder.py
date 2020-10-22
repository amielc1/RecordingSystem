import logging

import cv2
import numpy as np
import pyautogui

from Config.config_manager import ConfigManager


class ScreenRecorder():

    def __init__(self):
        cfg = ConfigManager()
        screen_recorder = cfg.get_configuration_of('screen_recorder')
        self.name = 'screen_recorder'
        self.is_started = False
        self.codec = cv2.VideoWriter_fourcc(*screen_recorder.get('codec'))
        self.out = cv2.VideoWriter(screen_recorder.get('filename'),
                                   self.codec,
                                   float(screen_recorder.get('frame_per_second')),
                                   pyautogui.size())

    # TODO: work on event start and stop record
    def record(self):
        # while self.is_started:
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

    def start(self):
        self.is_started = True
        self.record()
        logging.debug("Start record Screens")

    def stop(self):
        self.is_started = False
        logging.debug("Stop record Screens")

# screen_recorder = ScreedRecorder()
# screen_recorder.Start()
# screen_recorder.Stop()
