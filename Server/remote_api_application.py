import logging

from Agent.RemoteAPIServer import RemoteAPIServer
from Agent.agent import Agent
from Config.config_manager import ConfigManager
from Recorders.LogRecorder import LogRecorder
from Recorders.LogWriter import LogWriter
from Recorders.screen_recorder import ScreenRecorder

logging.basicConfig(filename='RemoteAPIApplication.log', filemode='w',
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logging.debug("------Remote API Application Start ----------")

cfg = ConfigManager()


def create_recorders() -> list:
    log_recorder_cfg = cfg.get_configuration_of('log_recorder')
    logging.debug("log_recorder_cfg Done! ")

    log_writer_cfg = cfg.get_configuration_of('log_writer')
    logging.debug("log_writer_cfg Done! ")

    log_recorder = LogRecorder(log_recorder_cfg.get('source'),
                               log_recorder_cfg.get('destination'),
                               log_recorder_cfg.get('interval'),
                               log_recorder_cfg.get('extension'),
                               'log_recorder')

    logging.debug("LogRecorder Created")
    log_writer = LogWriter(log_writer_cfg.get('destination'), log_writer_cfg.get('interval'),
                           log_writer_cfg.get('filename'),
                           'log_writer')
    logging.debug("LogWriter Created")

    screen_recorder = ScreenRecorder()
    logging.debug("Screen Recorder Created")

    recorders = [log_writer, log_recorder]  # , screen_recorder]
    return recorders


def get_agents():
    return agent


def perform_agent(name, method: str):
    getattr(agent, method)()


def perform_recorder(name, method: str):
    recorder = [recorder for recorder in recorders if recorder.name == name][0]
    getattr(recorder, method)()


recorders = create_recorders()
agent = Agent("Main Agent", recorders)

# agent.start()
#
# agent.stop()


remote_api_cfg = cfg.get_configuration_of('remote_api_config')

api_server = RemoteAPIServer(remote_api_cfg.get('ip'), remote_api_cfg.get('port'))
logging.debug("Create RemoteAPIServer")
api_server.register_function(get_agents)
api_server.register_function(perform_agent)
api_server.register_function(perform_recorder)
api_server.start_listen()
