import glob
import os
import shutil
from datetime import datetime
from pathlib import Path
from threading import Timer

import yaml


class LogRecorderConfig:

    def __init__(self):
        self.source = ""
        self.destination = ""
        self.interval = ""

    def create(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            logrecorder = data['log_recorder']
            lig = {}
            for rec in logrecorder:
                print(rec)
                lig[rec]
            # self.source = logrecorder[0]['source']
            # self.destination = logrecorder[1]['destination']
            # self.interval = logrecorder[2]['interval']


l = LogRecorderConfig()
l.create("recorder.yaml")
print(l.destination)
print(l.interval)
print(l.source)
input()


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class LogRecorder:

    def __init__(self, source, destination, interval):
        self.source = source
        self.destination = destination
        self.interval = interval
        self.timer = RepeatedTimer(3, self.copy_logs)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def copy_logs(self):
        for filename in glob.glob(os.path.join(self.source, '*.log')):
            shutil.copy(filename, self.destination)


class LogWriter:
    def __init__(self, destination, interval, filename):
        self.destination = destination
        self.interval = interval
        self.filename = filename
        self.timer = RepeatedTimer(1, self.write_log)

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


class Agent:

    def __init__(self):
        self.recorders = []

    def init_recorders(self, recorders: list):
        self.recorders = recorders

    def start(self):
        for recorder in self.recorders:
            recorder.start()

    def stop(self):
        for recorder in self.recorders:
            recorder.stop()


current_dir = Path().absolute()
log_recorder = LogRecorder(current_dir, "c:/tmp", 2)
log_writer = LogWriter(current_dir, 2, "Applog.log")
recorders = [log_writer, log_recorder]
agent = Agent()
agent.init_recorders(recorders)
agent.start()
input("type to stop")
agent.stop()
