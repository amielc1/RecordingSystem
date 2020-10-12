import yaml


class Remote_api_config:

    def __init__(self):
        self.ip: str
        self.port: int

    def parse(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            log_dic = {}
            for rec in data['remote_api_config']:
                log_dic.update(rec)
            self.ip = log_dic['ip']
            self.port = log_dic['port']
