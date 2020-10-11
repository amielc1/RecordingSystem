import logging

from Agent.RemoteAPIServer import RemoteAPIServer
from Agent.agent import Agent
from Config.LogRecorderConfig import LogRecorderConfig
from Config.LogWriterConfig import LogWriterConfig
from Config.remote_api_config import Remote_api_config
from Recorders.LogRecorder import LogRecorder
from Recorders.LogWriter import LogWriter

logging.StreamHandler()

remote_api_cfg = Remote_api_config()
remote_api_cfg.parse("Config/server.yml")
logging.info("remote_api_cfg Done! ")

log_recorder_cfg = LogRecorderConfig()
log_recorder_cfg.parse('Config/recorder.yml')
logging.info("log_recorder_cfg Done! ")

log_writer_cfg = LogWriterConfig()
log_writer_cfg.parse('Config/recorder.yml')
logging.info("log_writer_cfg Done! ")

api_server = RemoteAPIServer(remote_api_cfg.ip, remote_api_cfg.port)
logging.info("Create RemoteAPIServer")
log_recorder = LogRecorder(log_recorder_cfg.source, log_recorder_cfg.destination, log_recorder_cfg.interval,
                           log_recorder_cfg.extension)
logging.info("Create LogRecorder")
log_writer = LogWriter(log_writer_cfg.destination, log_writer_cfg.interval, log_writer_cfg.filename)
logging.info("Create LogWriter")
recorders = [log_writer, log_recorder]
agent = Agent("Main Agent", recorders)

api_server.register_function(agent.start)
api_server.register_function(agent.stop)
api_server.start_listen()
