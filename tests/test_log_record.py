import glob
import os
import shutil
from pathlib import Path
from LogRecorder import LogRecorder


# def arrange_test():
#     pass
#
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
#
#
# def test_copy_logs_by_extention_pass():
#     # arrange
#     current_dir = Path().absolute()
#     dest_file = os.path.join(Path().absolute(), 'out')
#     extn = '*.log'
#     if os.path.isdir(dest_file):
#         shutil.rmtree(dest_file)
#     # act
#     log_recorder = LogRecorder(current_dir, dest_file, 2, extn)
#     log_recorder.copy_logs()
#     # assert
#     matching = [s for s in glob.glob(os.path.join(dest_file, extn)) if "test_log_record.py" in s]
#     assert len(matching) == 0

def test_pass():
    assert  1 == 1