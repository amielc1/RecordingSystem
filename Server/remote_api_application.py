import logging

from Agent.RemoteAPIServer import RemoteAPIServer
from Agent.agent import Agent
from Config.LogRecorderConfig import LogRecorderConfig
from Config.LogWriterConfig import LogWriterConfig
from Config.remote_api_config import Remote_api_config
from Recorders.LogRecorder import LogRecorder
from Recorders.LogWriter import LogWriter

logging.basicConfig(filename='RemoteAPIApplication.log', filemode='w',
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logging.debug("------Remote API Application Start ----------")


def create_recorders(config_file: str) -> list:
    log_recorder_cfg = LogRecorderConfig()
    log_recorder_cfg.parse(config_file)
    logging.debug("log_recorder_cfg Done! ")

    log_writer_cfg = LogWriterConfig()
    log_writer_cfg.parse(config_file)
    logging.debug("log_writer_cfg Done! ")

    log_recorder = LogRecorder(log_recorder_cfg.source, log_recorder_cfg.destination, log_recorder_cfg.interval,
                               log_recorder_cfg.extension, log_recorder_cfg.name)
    logging.debug("Create LogRecorder")
    log_writer = LogWriter(log_writer_cfg.destination, log_writer_cfg.interval, log_writer_cfg.filename,
                           log_writer_cfg.name)
    logging.debug("Create LogWriter")
    recorders = [log_writer, log_recorder]
    return recorders


def get_agents():
    return agent


def perform_agent(name, method: str):
    getattr(agent, method)()


def perform_recorder(name, method: str):
    recorder = [recorder for recorder in recorders if recorder.name == name][0]
    getattr(recorder, method)()


recorders = create_recorders('../Config/recorder.yml')
agent = Agent("Main Agent", recorders)

remote_api_cfg = Remote_api_config()
remote_api_cfg.parse("../Config/server.yml")
logging.debug("remote_api_cfg Done! ")

api_server = RemoteAPIServer(remote_api_cfg.ip, remote_api_cfg.port)
logging.debug("Create RemoteAPIServer")
api_server.register_function(get_agents)
api_server.register_function(perform_agent)
api_server.register_function(perform_recorder)
api_server.start_listen()
