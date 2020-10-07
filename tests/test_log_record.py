import glob
from pathlib import Path

from LogRecorder import LogRecorder


def test_copy_logs_pass():
    current_dir = Path().absolute()
    dest_file = "c:/tmp"
    extn = '*.*'
    log_recorder = LogRecorder(current_dir, dest_file, 2, extn)
    log_recorder.copy_logs()
    lst = [filename for filename in glob.glob(os.path.join(dest_file, extn))]
    for item in lst:
        assert "LogRecorder" in item


def test_cpy_files1():
    assert len('fff') < 1


test_copy_logs_pass()
