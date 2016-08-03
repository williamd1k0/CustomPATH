# -*- encoding: utf-8 -*-


import sys
import os.path
import cplib


def main(argv):
    if len(argv) > 1:
        args = argv[1:]
        if len(args) == 1:
            args = []
        else:
            args = args[1:]
        sys.exit(cplib.show_path(argv[1].split('\\')[-1], args))


    elif os.path.isfile(cplib.DATA):
        cplib.print_list()


if __name__ == '__main__':
    main(argv)