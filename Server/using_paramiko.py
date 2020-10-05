import os
from stat import S_ISDIR

import paramiko


def isdir(path):
    try:
        return S_ISDIR(sftp.stat(path).st_mode)
    except IOError:
        # Path does not exist, so by definition not a directory
        return False


paramiko.util.log_to_file("paramiko.log")

# Open a transport
host, port = '127.0.0.1', 22
transport = paramiko.Transport((host, port))

# Auth
username, password = "Me", ""
transport.connect(None, username, password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)

log_dir = 'Downloads\log_files_dir'
file_list = sftp.listdir(path=log_dir)
print(file_list)
for file in file_list:
    print(os.path.join(log_dir, file))
    print(os.path.join(os.getcwd(), file))
    sftp.get(os.path.join(log_dir, file), os.path.join(os.getcwd(), file))

# # Upload
# filepath = "/home/foo.jpg"
# localpath = "/home/pony.jpg"
# sftp.put(localpath,filepath)

# Close
if sftp: sftp.close()
if transport: transport.close()
