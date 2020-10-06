import os
from stat import S_ISDIR

import paramiko


class get_remote_files_config:

    def __init__(self, ip: str, port: int, username: str, password: str):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password


class get_remote_files:

    def __init__(self, config: get_remote_files_config):
        self.config = config
        self.transport: paramiko.Transport
        self.sftp: paramiko.SFTPClient

    def connect(self):
        self.transport = paramiko.Transport((self.config.ip, self.config.port))
        self.transport.connect(None, self.config.username, self.config.password)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def isdir(path):
        try:
            return S_ISDIR(sftp.stat(path).st_mode)
        except IOError:
            # Path does not exist, so by definition not a directory
            return False

    def get_files(self, src: str, dst: str):
        file_list = sftp.listdir(path=src)
        for file in file_list:
            self.sftp.get(os.path.join(src, file), os.path.join(dst, file))

    def close(self):
        if self.sftp: self.sftp.close()
        if self.transport: self.transport.close()


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

log_dir = 'c:/tmp'
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
