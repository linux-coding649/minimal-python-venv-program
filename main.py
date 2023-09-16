# Created by linux649 under the GNU GPLv3 License

# VEP (Virtual Environment Program)  Copyright (C) 2023  linux649
# This program comes with ABSOLUTELY NO WARRANTY; for details go to <https://www.gnu.org/licenses>'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; go to <https://www.gnu.org/licenses> for details.

from sys import exit

def log(procid, msg):
    print(f'[LOG-{procid}]: {msg}')


try:
    import loaders.cmd_loader
    import loaders.config_loader
except ImportError:
    log('start', 'unable to import loaders, are you missing files?')
    log('error', 'failed to start VEP, unable to import required loaders')
    log('end', 'exit-code 1')
    exit(1)
import importlib


ALLOW_EXTCMD = True
CFG_FILE = 'config.ini'

try:
    f = open(CFG_FILE, 'r')
    f.close()
    RFILE, RLOCA = loaders.config_loader.readConfig(CFG_FILE)
except FileNotFoundError:
    loaders.config_loader.createConfig(CFG_FILE)

if not RFILE or not RLOCA:
    log('start', 'external commands are NOT being allowed, incorrect configuration')
    ALLOW_EXTCMD=False



help = '''builtin commands:
          help                 | Shows this help menu
          ?                    | Shows this help menu
          extc                 | Uses an external command library
          creg                 | (Re)Creates the external command registry
          hist                 | Shows current session command history
          exit                 | Exits this VEP (Virtual Environment Program)
          stop                 | Exits this VEP (Virtual Environment Program)
          quit                 | Exits this VEP (Virtual Environment Program)'''

cmdHistory = []
log('start', 'Loading libraries')
log('start', 'Starting Virtual Environment Program')
log('start', 'Terminal Started')


while True:
    try:
        cmd = input("% ")
        cmdHistory.append(cmd)
        log('cmd-prm', f'executed command {cmd}')
        if cmd == 'help' or cmd == '?':
            print(help)
        elif cmd == 'extc':
            if ALLOW_EXTCMD:
                loaded = loaders.cmd_loader.loadRegistry(RFILE, RLOCA)
                if loaded == 1:
                    continue
                rid = input('registry id: ')
                if rid not in loaded:
                    log('cmd_loader', 'no such registry-id')
                    continue
                cmmd = input(f'{rid} command: ')
                libx = importlib.import_module(f'{RLOCA}.{rid}')
                cmdHistory.append(f'[{rid}]: {cmmd}')
                try:
                    err = libx.__command__(cmmd)
                    if err:
                        log('cmd-prm', 'Command Not Found')
                except NameError:
                    log('cmd-prm', f'unable to execute {rid} commands, no __command__ function')
                except TypeError:
                    log('cmd-prm', f'unable to execute {rid} commands, no __command__ function')
                except AttributeError:
                    log('cmd-prm', f'unable to execute {rid} commands, no __command__ function')
            else:
                log('cmd-prm', 'unable to execute extc, external commands are not allowed')
        elif cmd == 'creg':
            if ALLOW_EXTCMD:
                ms = input('Are you sure you want to clear current registries and create a new one? [y/N]: ')
                if ms.lower() == 'y':
                    loaders.cmd_loader.createRegistry(RFILE)
                else:
                    log('cmd-prm', 'aborted registry creation')
            else:
                log('cmd-prm', 'unable to execute creg, external commands are not allowed')
        elif cmd == 'hist':
            for i in cmdHistory:
                print(i)
        elif cmd == 'exit' or cmd == 'stop' or cmd == 'quit':
            log('cmd-prm', 'Terminal Stopped')
            log('code', 'Loop Broken')
            break
        else:
            log('cmd-prm', 'Command Not Found')
    except KeyboardInterrupt:
        log('key-detect', 'CTRL-C has been detected and ignored')
    except EOFError:
        log('key-detect', 'CTRL-D has been detected and ignored')
log('end', 'Stopped Virtual Environment Program')
log('end', 'exit-code 0')
exit(0)
