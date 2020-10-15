# https://www.tocode.co.il/past_workshops/24
import xmlrpc.client as xmlrpclib

from flask import Flask, render_template

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
    return "redirect(‘/‘)"


if __name__ == '__main__':
    agent = proxy.get_agents()
    app.run()
