import glob
import os

from Recorders.LogRecorder import LogRecorder


def test_logRecorder_copy_logs_pass(tmpdir_factory):
    # arrange
    src = tmpdir_factory.mktemp("src")
    dst = tmpdir_factory.mktemp("dst")
    extn = '*.*'
    my_file_name = 'amico.py'
    p = src.join(my_file_name)
    p.write("content")
    # act
    log_recorder = LogRecorder(src, dst, 2, extn)
    log_recorder.copy_logs()
    # assert
    matching = [s for s in glob.glob(os.path.join(dst, extn)) if my_file_name in s]
    assert len(matching) > 0


def test_logRecorder_copy_logs_by_extention_pass(tmpdir_factory):
    # arrange
    src = tmpdir_factory.mktemp("src")
    dst = tmpdir_factory.mktemp("dst")
    extn = '*.log'
    my_file_name = 'amico.py'
    p = src.join(my_file_name)
    p.write("content")
    # act
    log_recorder = LogRecorder(src, dst, 2, extn)
    log_recorder.copy_logs()
    # assert
    matching = [s for s in glob.glob(os.path.join(dst, extn)) if my_file_name in s]
    assert len(matching) == 0

# def write_to_log():
#     src = tmpdir_factory.mktemp("src")
#
#
# def test_logRecorder_start_record(tmpdir_factory):
#     # the recorder should to collect files periodically.
#     # arrange
#     src = tmpdir_factory.mktemp("src")
#
#     # act
#     log_recorder = LogRecorder(src, dst, 2, extn)
#     log_recorder.start()
#     # assert
