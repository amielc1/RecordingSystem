import yaml


class get_remote_files_config:

    def __init__(self):
        self.ip: str
        self.port: int
        self.username: str
        self.password: str

    def parse(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            log_dic = {}
            for rec in data['get_remote_files']:
                log_dic.update(rec)
            self.ip = log_dic['ip']
            self.port = log_dic['port']
            self.username = log_dic['username']
            self.password = log_dic['password']
