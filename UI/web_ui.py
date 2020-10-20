# https://www.tocode.co.il/past_workshops/24
import xmlrpc.client as xmlrpclib

from flask import Flask, render_template, redirect, url_for

from Config.get_remote_files_config import Get_remote_files_config
from Server.get_remote_files import get_remote_files

app = Flask('Recording System')
global agent

proxy = xmlrpclib.ServerProxy('http://localhost:9000')


@app.route('/')
def index():
    return render_template('index.html', agent_name=agent['name'],
                           recorders=agent['recorders'])


@app.route('/agents/<string:name>/<string:state>', methods=['POST'])
def user_view(name, state):
    recorders = agent['recorders']
    proxy.perform_recorder(name, state)
    return redirect(url_for('index'))


@app.route('/get_remote_files', methods=['POST'])
def get_files():
    remote_config = Get_remote_files_config()
    remote_config.parse('../Config/server.yml')
    remote = get_remote_files(remote_config)
    remote.connect()
    remote.get_files('C:/dest', 'C:/SSh_dir')
    return redirect(url_for('index'))


if __name__ == '__main__':
    agent = proxy.get_agents()
    app.run()
