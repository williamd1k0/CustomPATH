# -*- encoding: utf-8 -*-


import sys
import os.path
import cplib
import multiprocessing


def main(argv):
    if len(argv) > 1:
        args = argv[1:]
        if len(args) == 1:
            args = []
        else:
            args = args[1:]
        cplib.exec_nowait(argv[1].split('\\')[-1], args)
        sys.exit(0)


    elif os.path.isfile(cplib.DATA):
        cplib.print_list()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main(sys.argv)
