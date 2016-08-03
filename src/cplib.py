# -*- encoding: utf-8 -*-


import sys
import os.path
import subprocess
from multiprocessing import Process


__version__ = (0, 4, 0)

if 'python.exe' in sys.executable:
    PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
else:
    PATH = os.path.dirname(os.path.realpath(sys.executable))
DATA = os.path.join(PATH, 'custom_path.csv')


def print_list():
    progs = None
    with open(DATA, 'r', encoding='utf-8') as apps:
        progs = apps.read().split('\n')
    del apps
    for prg in range(1, len(progs)):
        print(progs[prg].split(',')[0])


def exec_program(prog, args):
    return subprocess.call('"%s" %s' % (search_program(prog), ' '.join(args)), shell=True)


def nowait_process(args):
     pid = subprocess.Popen(args).pid
    

def exec_nowait(prog, args_):
    progfull = search_program(prog)
    arglist = list()
    arglist.append(progfull)
    if len(args_) > 0:
        arglist.append(args_)
    process = Process(target=nowait_process, args=[arglist])
    process.start()
    sys.exit(0)


def show_path(prog, args):
    print('"%s" %s' % (search_program(prog), ' '.join(args)))


def search_program(prog):
    if not os.path.isfile(DATA):
        raise NoProgramListException()
    
    progs = None
    with open(DATA, 'r', encoding='utf-8') as apps:
        progs = apps.read()
    del apps

    proglist = progs.split('\n')[1:]
    for progitem in proglist:
        if prog+'.' in progitem:
            return progitem.split(',')[1]
    else:
        raise ProgramNotFoundException()
    

def add_program(prog, path):
    duplicate = False
    if not os.path.isfile(DATA):
        with open(DATA, 'w', encoding='utf-8') as apps:
            apps.write('program,path')
        del apps
    
    with open(DATA, 'r', encoding='utf-8') as apps:
        if prog in apps.read():
            duplicate = True
    del apps
    if duplicate:
        raise DuplicateProgramException()
 
    with open(DATA, 'a', encoding='utf-8') as apps:
        apps.write('\n%s,%s' % (prog, path))
    del apps
    return True


class NoProgramListException(Exception):
    pass


class ProgramNotFoundException(Exception):
    pass


class DuplicateProgramException(Exception):
    pass