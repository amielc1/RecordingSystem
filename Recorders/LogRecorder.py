import glob
import logging
import os
import shutil

from Utils import RepeatedTimer as rt


class LogRecorder:

    def __init__(self, source: str, destination: str, interval: int, extension: str, name: str):
        self.source = source
        self.destination = destination
        self.interval = int(interval)
        self.extension = extension
        self.timer = rt.RepeatingTimer(self.interval, self.copy_logs)
        self.name = name
        logging.debug(f"Create {self.name}")

    def start(self):
        logging.debug(f"start {self.name}")
        self.timer.start()

    def stop(self):
        logging.debug(f"stop {self.name}")
        self.timer.stop()

    def copy_logs(self):
        if not os.path.isdir(self.destination):
            os.mkdir(self.destination)
        for filename in glob.glob(os.path.join(self.source, self.extension)):
            shutil.copy(filename, self.destination)
