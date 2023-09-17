# Created by linux649 under the GNU GPLv3 License

# VEP (Virtual Environment Program) Launcher Copyright (C) 2023  linux649
# This program comes with ABSOLUTELY NO WARRANTY; for details go to <https://www.gnu.org/licenses>'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; go to <https://www.gnu.org/licenses> for details.

def log(procid, msg):
    print(f'[LOG-{procid}]: {msg}')


log('launcher-import', 'Loading libraries')

from sys import exit
import urllib.request
import urllib.error
try:
    import core.__main__
except ImportError:
    log('launcher-import', 'Launcher failed to start, unable to load core VEP Programs')
    log('launcher-import', 'Are you missing files?')
    log('end', 'exit-code 1')
    exit(1)


log('launcher', 'Starting launcher...')

help = '''launcher commands:
              help                 | Shows this help menu
              start                | Starts the VEP
              download             | Downloads a specified version of the VEP from GitHub
              exit                 | Exits this launcher
'''

while True:
    try:
        cmd = input('launcher> ')
        if cmd == 'help':
            print(help)
        elif cmd == 'start':
            log('launcher', 'starting VEP')
            core.__main__.main()
        elif cmd == 'download':
            log('launcher', 'downloading VEP')
            ver = input('semantic version: ')
            try:
                urllib.request.urlretrieve(f'https://github.com/linux-coding649/minimal-python-venv-program/archive/refs/tags/v{ver}.zip',
                                           f'VEP-download-{ver}.zip')
            except urllib.error.HTTPError:
                log('downloader', 'invalid version, not downloading')
        elif cmd == 'exit':
            log('launcher', 'Launcher Stopped')
            break
        elif cmd == '':
            continue
        else:
            log('launcher', 'Command Not Found')
    except KeyboardInterrupt:
        log('key-detect', 'CTRL-C detected and ignored')
    except EOFError:
        log('key-detect', 'CTRL-D detected and ignored')

log('end', 'exit-code 0')
exit(0)
