import os
import toml


class ConfigFile(object):
    def __init__(self):
        self.globals = dict()
        self.acls = []
        self.views = []
        self.zones = []

    def Initialize(self, data: dict) -> (bool, [str, None]):
        return False, ''

    @staticmethod
    def LoadFile(path: str) -> ([dict, None], [str, None]):
        if not path or not os.path.isfile(path):
            return None, 'invalid file path'

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = toml.load(f)
        except IOError as e:
            return None, 'failed to read config file: {}'.format(e)
        except toml.TomlDecodeError as e:
            return None, 'failed to decode file: {}'.format(e)

        return data, None


def LoadConfigFile(path: str) -> ([ConfigFile, None], [str, None]):
    data, err = ConfigFile.LoadFile(path)

    if err:
        return None, err

    config = ConfigFile()
    result, err = config.Initialize(data)

    if not result:
        return None, err

    return config, None
