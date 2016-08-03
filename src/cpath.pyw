# -*- encoding: utf-8 -*-

import sys
import os.path
import subprocess

DATA = 'C:\\custom_path\custom_path.csv'

def exec_program(prog, args):
    if not os.path.isfile(DATA):
        return 1
    
    progs = None
    with open(DATA, 'r') as apps:
        progs = apps.read()
    del apps

    proglist = progs.split('\n')[1:]
    for progitem in proglist:
        if prog+'.' in progitem:
            return exec_(progitem.split(',')[1], args)
    else:
        return -1

def exec_(prog, args):
    subprocess.call("%s %s" % (prog, ' '.join(args)), shell=True)
    return 0

def print_list():
    progs = None
    with open(DATA, 'r') as apps:
        progs = apps.read().split('\n')
    del apps
    for prg in range(1, len(progs)):
        print(progs[prg].split(',')[0])


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        try:
            args = sys.argv[1:]
            if len(args) == 1:
                args = ''
            else:
                args = args[1:]
            sys.exit(exec_program(sys.argv[1].split('\\')[-1], args))
        except Exception as e:
            raise
    elif os.path.isfile(DATA):
        print_list()
