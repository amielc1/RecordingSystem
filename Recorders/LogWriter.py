import logging
from datetime import datetime
from pathlib import Path

from Utils import RepeatedTimer as rt


class LogWriter:
    def __init__(self, destination, interval, filename, name: str):
        self.destination = destination
        self.interval = interval
        self.filename = filename
        self.timer = rt.RepeatedTimer(1, self.write_log)
        self.name = name
        logging.debug(f"Create {self.name}")

    def start(self):
        logging.debug(f"start {self.name}")
        self.timer.start()

    def stop(self):
        logging.debug(f"stop {self.name}")
        self.timer.stop()

    def write_log(self):
        location = Path().joinpath(self.destination, self.filename)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(location, 'a') as f:
            f.write(dt_string)
            f.write('\n')
