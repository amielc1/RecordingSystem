from pathlib import Path

import Agent.agent as agnt
from Agent import RemoteAPIServer as ras
from Recorders.LogRecorder import LogRecorder
from Recorders.LogWriter import LogWriter

api_server = ras.RemoteAPIServer('127.0.0.1', 9000)
current_dir = Path().absolute()
log_recorder = LogRecorder(current_dir, "c:/tmp", 2, '*.log')
log_writer = LogWriter(current_dir, 2, "Applog.log")
recorders = [log_writer, log_recorder]
agent = agnt.Agent(recorders)
api_server.register_function(agent.start)
api_server.register_function(agent.stop)
api_server.start_listen()
