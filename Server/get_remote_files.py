import os
from stat import S_ISDIR

import paramiko

from Config.config_manager import ConfigManager


class get_remote_files:

    def __init__(self):
        cfg = ConfigManager().get_configuration_of('get_remote_files_config')
        self.ip = cfg.get('ip')
        self.port = int(cfg.get('port'))
        self.username = cfg.get('username')
        self.password = cfg.get('password')
        self.transport: paramiko.Transport
        self.sftp: paramiko.SFTPClient

    def connect(self):
        self.transport = paramiko.Transport((self.ip, self.port))
        self.transport.connect(None, self.username, self.password)
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