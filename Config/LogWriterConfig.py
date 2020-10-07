import yaml


class LogWriterConfig:

    def __init__(self):
        self.destination: str
        self.interval: int
        self.filename: str

    def parse(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            log_rec_dic = {}
            for rec in data['log_writer']:
                log_rec_dic.update(rec)
            self.filename = log_rec_dic['filename']
            self.destination = log_rec_dic['destination']
            self.interval = log_rec_dic['interval']

# l = LogWriterConfig()
# l.parse("recorder.yaml")
# print(l.destination)
# print(l.filename)
