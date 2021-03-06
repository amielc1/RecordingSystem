import logging


class Agent:
    def __init__(self, name: str, recorders: list):
        self.recorders = recorders
        self.name = name
        logging.debug(f"Create Agent {self.name} with {len(self.recorders)} recorders")

    def start(self):
        logging.debug("start agent...")
        self.invoke_on_all_recorders('start')

    def stop(self):
        logging.debug("stop agent...")
        self.invoke_on_all_recorders('stop')

    def invoke_on_all_recorders(self, method_name: str, *args):
        for recorder in self.recorders:
            getattr(recorder, method_name)(*args)
