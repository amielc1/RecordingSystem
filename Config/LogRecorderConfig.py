import yaml


class LogRecorderConfig:

    def __init__(self):
        self.source: str
        self.destination: str
        self.interval: int
        self.extension: str
        self.name: str = 'log_recorder'

    def parse(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            log_rec_dic = {}
            for rec in data[self.name]:
                log_rec_dic.update(rec)
            self.source = log_rec_dic['source']
            self.destination = log_rec_dic['destination']
            self.interval = log_rec_dic['interval']
            self.extension = log_rec_dic['extension']

# l = LogRecorderConfig()
# l.parse("recorder.yml")
# print(l.source)
# print(l.extension)
