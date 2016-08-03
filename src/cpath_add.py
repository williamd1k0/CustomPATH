# -*- encoding: utf-8 -*-


import sys
import os.path
import cplib


def main(argv):
    if len(argv) > 1:
        cplib.add_program(argv[1].split('\\')[-1], argv[1])

    elif os.path.isfile(cplib.DATA):
        cplib.print_list()


if __name__ == '__main__':
    main(sys.argv)

