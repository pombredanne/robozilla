import os
import sys

from robozilla.parser import Parser


def main():
    _current_environment_path = os.path.realpath(os.path.curdir)
    scan_dir = _current_environment_path
    print(_current_environment_path)

    if len(sys.argv) > 1:
        scan_dir = sys.argv[1]
    else:
        # print('please supply dir to scan')
        # print('usage: parse.py dir_to_parse_path')
        # sys.exit(2)
        pass

    parser = Parser(
        scan_dir,
        filters=None,
        reporter=None,
        bz_reader=None,
        enviroment=None
    )
    parser.parse()


if __name__ == '__main__':
    main()
