# -*- encoding: utf-8 -*-

import sys
import os.path

DATA = 'C:\\custom_path\custom_path.csv'

def add_program(prog, path):
    duplicate = False
    if not os.path.isfile(DATA):
        with open(DATA, 'w') as apps:
            apps.write('program,path')
        del apps
    
    with open(DATA, 'r') as apps:
        if prog in apps.read():
            duplicate = True
    del apps
    if duplicate:
        return 1
 
    with open(DATA, 'a') as apps:
        apps.write('\n{},{}'.format(prog, path))
    del apps
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
            sys.exit(add_program(sys.argv[1].split('\\')[-1], sys.argv[1]))
        except Exception as e:
            print(e)
    elif os.path.isfile(DATA):
        print_list()
