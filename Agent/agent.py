
class Agent:

    def __init__(self):
        self.recorders = []

    def init_recorders(self, recorders: list):
        self.recorders = recorders

    def start(self):
        print("start agent")
        for recorder in self.recorders:
            recorder.start()

    def stop(self):
        for recorder in self.recorders:
            recorder.stop()
