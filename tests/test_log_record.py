import glob
from pathlib import Path

from LogRecorder import LogRecorder


def test_copy_logs_pass():
    current_dir = Path().absolute()
    log_recorder = LogRecorder(current_dir, "c:/tmp", 2, '*.*')
    log_recorder.copy_logs()
    for filename in glob.glob(current_dir):
        print(filename)


def test_cpy_files1():
    assert len('fff') < 1


test_copy_logs_pass()
