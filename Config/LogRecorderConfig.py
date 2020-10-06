import yaml


class LogRecorderConfig:

    def __init__(self):
        self.source: str
        self.destination: str
        self.interval: int

    def create(self, filename):
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            logrecorder = data['log_recorder']
            log_rec_dic = {}
            for rec in logrecorder:
                for key in rec:
                    print(f"{key} : {rec[key]}")
                    log_rec_dic[key] = rec[key]
        print(log_rec_dic)

        # self.source = logrecorder[0]['source']
        # self.destination = logrecorder[1]['destination']
        # self.interval = logrecorder[2]['interval']

# l = LogRecorderConfig()
# l.create("recorder.yaml")
# print(l.destination)
# print(l.interval)
# print(l.source)
# input()
