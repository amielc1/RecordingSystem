class LogRecorder:
    def __init__(self, source, destination, interval):
        self.source = source
        self.destination = destination
        self.interval = interval

    def start(self):
        pass

    def stop(self):
        pass


class LogWriter:
    def __init__(self, destination, interval, filename):
        self.destination = destination
        self.interval = interval
        self.filename = filename

    def start(self):
        pass

    def stop(self):
        pass


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


log_recorder = LogRecorder()
log_writer = LogWriter()
recorders = [log_writer, log_recorder]
agent = Agent()
agent.init_recorders(recorders)
agent.start()
