# https://www.tocode.co.il/past_workshops/24
from flask import Flask, render_template

from Agent.agent import Agent
from Config.LogRecorderConfig import LogRecorderConfig
from Config.LogWriterConfig import LogWriterConfig
from Recorders.LogRecorder import LogRecorder
from Recorders.LogWriter import LogWriter

app = Flask('Recording System')


def get_recorders(config_file: str) -> list:
    log_recorder_cfg = LogRecorderConfig()
    log_recorder_cfg.parse(config_file)

    log_writer_cfg = LogWriterConfig()
    log_writer_cfg.parse(config_file)

    log_recorder = LogRecorder(log_recorder_cfg.source, log_recorder_cfg.destination, log_recorder_cfg.interval,
                               log_recorder_cfg.extension, log_recorder_cfg.name)
    log_writer = LogWriter(log_writer_cfg.destination, log_writer_cfg.interval, log_writer_cfg.filename,
                           log_writer_cfg.name)
    recorders = [log_writer, log_recorder]
    return recorders


def create_agent() -> Agent:
    recorders = get_recorders('recorder.yml')
    agent = Agent("Main Agent", recorders)
    return agent


@app.route('/')
def index():
    agent = create_agent()
    return render_template('index.html', agent_name=agent.name,
                           recorders=agent.recorders)


@app.route('/agents/<string:name>/<string:state>', methods=['GET', 'POST'])
def user_view(name, state):
    recorders = get_recorders('recorder.yml')
    recorder = [recorder for recorder in recorders if recorder.name == name][0]
    if state == 'start':
        recorder.start()
    if state == 'stop':
        recorder.stop()
    return "Done"


if __name__ == '__main__':
    app.run()
