import glob
import os

from LogRecorder.LogRecorder import LogRecorder


# def test_copy_logs_pass():
#     # arrange
#     current_dir = Path().absolute()
#     dest_file = os.path.join(Path().absolute(), 'out')
#     extn = '*.py'
#     if os.path.isdir(dest_file):
#         shutil.rmtree(dest_file)
#     # act
#     log_recorder = LogRecorder(current_dir, dest_file, 2, extn)
#     log_recorder.copy_logs()
#     # assert
#     matching = [s for s in glob.glob(os.path.join(dest_file, extn)) if "test_log_record.py" in s]
#     assert len(matching) > 0


def test_copy_logs_by_extention_pass(tmpdir_factory):
    # arrange
    src = tmpdir_factory.mktemp("src")
    dst = tmpdir_factory.mktemp("dst")
    extn = '*.log'
    # act
    log_recorder = LogRecorder(src, dst, 2, extn)
    log_recorder.copy_logs()
    # assert
    matching = [s for s in glob.glob(os.path.join(dst, extn)) if "test_log_record.py" in s]
    assert len(matching) == 0
