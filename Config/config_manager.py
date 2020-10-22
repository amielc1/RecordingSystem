import logging

import yaml


class ConfigManager:

    def __init__(self):
        self.data = {}
        self.__load_config_file__('../Config/config.yml')

    def __load_config_file__(self, filename):
        try:
            with open(filename) as f:
                self.data = yaml.load(f, Loader=yaml.FullLoader)
                logging.debug(f'{filename} file loaded')
        except:
            logging.error(f'error while loading {filename} file')

    def get_configuration_of(self, section: str) -> dict:
        temp_dic = {}
        for item in self.data[section]:
            temp_dic.update(item)
        return temp_dic

#
# cfg = ConfigManager().get_configuration_of('log_writer')
# interval = cfg.get('interval')
