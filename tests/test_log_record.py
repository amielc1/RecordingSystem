import glob
import os
from pathlib import Path

from Recorders.LogRecorder import LogRecorder


def test_logRecorder_copy_logs_pass(tmpdir_factory):
    # arrange
    src = Path().absolute()
    dst = tmpdir_factory.mktemp("dst")
    extn = '*.*'
    # act
    log_recorder = LogRecorder(src, dst, 2, extn)
    log_recorder.copy_logs()
    # assert
    matching = [s for s in glob.glob(os.path.join(dst, extn)) if "test_log_record.py" in s]
    assert len(matching) > 0


def test_logRecorder_copy_logs_by_extention_pass(tmpdir_factory):
    # arrange
    src = Path().absolute()
    dst = tmpdir_factory.mktemp("dst")
    extn = '*.log'
    # act
    log_recorder = LogRecorder(src, dst, 2, extn)
    log_recorder.copy_logs()
    # assert
    matching = [s for s in glob.glob(os.path.join(dst, extn)) if "test_log_record.py" in s]
    assert len(matching) == 0
