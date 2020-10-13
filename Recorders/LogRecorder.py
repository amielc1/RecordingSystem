import glob
import os
import shutil

from Utils import RepeatedTimer as rt


class LogRecorder:

    def __init__(self, source: str, destination: str, interval: int, extension: str, name: str):
        self.source = source
        self.destination = destination
        self.interval = interval
        self.extension = extension
        self.timer = rt.RepeatedTimer(self.interval, self.copy_logs)
        self.name = name

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def copy_logs(self):
        if not os.path.isdir(self.destination):
            os.mkdir(self.destination)
        for filename in glob.glob(os.path.join(self.source, self.extension)):
            shutil.copy(filename, self.destination)
