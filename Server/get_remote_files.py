import os
from stat import S_ISDIR

import paramiko

from Config.get_remote_files_config import Get_remote_files_config


class get_remote_files:

    def __init__(self, config: Get_remote_files_config):
        self.config = config
        self.transport: paramiko.Transport
        self.sftp: paramiko.SFTPClient

    def connect(self):
        self.transport = paramiko.Transport((self.config.ip, self.config.port))
        self.transport.connect(None, self.config.username, self.config.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def isdir(self, path):
        try:
            return S_ISDIR(self.sftp.stat(path).st_mode)
        except IOError:
            # Path does not exist, so by definition not a directory
            return False

    def get_files(self, src: str, dst: str):
        file_list = self.sftp.listdir(path=src)
        if len(file_list):
            if not os.path.isdir(dst):
                os.mkdir(dst)
        for file in file_list:
            self.sftp.get(os.path.join(src, file), os.path.join(dst, file))

    def close(self):
        if self.sftp:
            self.sftp.close()
        if self.transport:
            self.transport.close()

# remote_config = Get_remote_files_config()
# remote_config.parse('../Config/server.yml')
# remote = get_remote_files(remote_config)
# remote.connect()
# remote.get_files('C:/dest', 'C:/SSh_dir')
