import argparse
from bindtool.config import ConfigFile, LoadConfigFile

Command = 'generate'
Description = 'Generate the bind config from the given configuration'


def RunGenerateCommand(args: argparse.Namespace) -> bool:
    config, err = LoadConfigFile(args.config)

    if err:
        print('Failed to load configuration file: {}'.format(err))
        return False

    print(config)
    return True


def SetupCommand(cmd: argparse.ArgumentParser) -> None:
    cmd.add_argument('config', help='Path to the root server configuration file')
