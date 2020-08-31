from base_recorder import recorder_base

class log_recorder(recorder_base):

    def copy_files(self,src_dir):
        recorder_base.start_record()


    def __init__(self):
        recorder_base.__init__()

    def start_record(self):
        recorder_base.start_record()
