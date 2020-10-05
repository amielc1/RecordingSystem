import glob
import os
import shutil

from Utils import RepeatedTimer as rt


class LogRecorder:

    def __init__(self, source, destination, interval):
        self.source = source
        self.destination = destination
        self.interval = interval
        self.timer = rt.RepeatedTimer(3, self.copy_logs)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def copy_logs(self):
        for filename in glob.glob(os.path.join(self.source, '*.log')):
            shutil.copy(filename, self.destination)
