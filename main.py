# Press the green button in the gutter to run the script.
import glob
import os
import shutil
from mss import mss

if __name__ == '__main__':
    print("hi")
    src  = "BaseRecorder"
    dest = "ScreenRecoder"
    src_files = os.listdir(src)
    print(src_files)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)



