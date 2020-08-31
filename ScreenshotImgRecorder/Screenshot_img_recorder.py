from mss import mss
from datetime import date



class Screenshot_img_recorder_config():
    def __init__(self,filename,monitor_num,recordHz=1):
        self.filename =filename
        self.recordHz=recordHz
        self.monitor_num = monitor_num

class Screenshot_img_recorder():
    def __init__(self,Screenshot_img_recorder_config):
        self.filename = Screenshot_img_recorder_config.filename
        self.recordHz = Screenshot_img_recorder_config.recordHz
        self.monitor_num =  Screenshot_img_recorder_config.monitor_num

    #TODO : how using python timers
    def Start(self):
        with mss() as sct:
            name = f"{self.filename}_{date.today().ctime()}.png".replace(" ", "_").replace(":", "_")
            sct.shot(mon=self.monitor_num, output=name)

    def Stop(self):
        pass

scrn_cfg = Screenshot_img_recorder_config(filename="Amie",monitor_num=-1)
recorder = Screenshot_img_recorder(scrn_cfg)
recorder.Start()
recorder.Start()
recorder.Start()