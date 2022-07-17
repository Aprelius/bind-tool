import argparse
import sys

import bindtool.cli.generate as generate


def Main() -> bool:
    parser = argparse.ArgumentParser("bind-tool")
    commands = parser.add_subparsers(dest='command')

    generate.SetupCommand(
        commands.add_parser(generate.Command,
                            help=generate.Description))

    args = parser.parse_args()
    if args.command == generate.Command:
        return generate.RunGenerateCommand(args)

    parser.print_help(sys.stderr)
    return False


if __name__ == '__main__':
    if not Main():
        sys.exit(1)
