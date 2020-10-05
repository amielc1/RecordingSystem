from pathlib import Path
from xmlrpc.server import SimpleXMLRPCServer

from LogRecorder import LogRecorder
from LogWriter import LogWriter


class Agent:

    def __init__(self):
        self.recorders = []
        self.server = SimpleXMLRPCServer(('localhost', 9000), allow_none=True)

    def init_recorders(self, recorders: list):
        self.recorders = recorders
        self.server.register_function(self.start)
        self.server.serve_forever()

    def start(self):
        print("start agent")
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
# agent.start()
# input("type to stop")
# agent.stop()
