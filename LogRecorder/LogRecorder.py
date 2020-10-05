import yaml

with open('../Agent/recorder.yaml') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)
    mymap = yaml.dump(yaml.load(f))
    a = 1

# from base_recorder import recorder_base
#
#
# class LogRecorder(recorder_base):
#
#     def __init__(self):
#         recorder_base.__init__()
#
#     def copy_files(self, src_dir):
#         recorder_base.start_record()
#
#     def start_record(self):
#         recorder_base.start_record()
