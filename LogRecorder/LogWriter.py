from datetime import datetime
from pathlib import Path

from Utils import RepeatedTimer as rt


class LogWriter:
    def __init__(self, destination, interval, filename):
        self.destination = destination
        self.interval = interval
        self.filename = filename
        self.timer = rt.RepeatedTimer(1, self.write_log)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def write_log(self):
        location = Path().joinpath(self.destination, self.filename)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(location, 'a') as f:
            f.write(dt_string)
            f.write('\n')
