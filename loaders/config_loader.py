# Created by linux649 under the GNU GPLv3 License

# VEP (Virtual Environment Program) Configuration Loader Copyright (C) 2023  linux649
# This program comes with ABSOLUTELY NO WARRANTY; for details go to <https://www.gnu.org/licenses>'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; go to <https://www.gnu.org/licenses> for details.

import configparser

def createConfig(cfile):
    cfg = configparser.ConfigParser()
    cfg['External Commands'] = {'registry-json':'registry.external.json',
                                'library-dir': 'extCmds',
                                'compressed-dir':'cmpCmds'}
    with open(cfile, 'w') as cfgf:
        cfg.write(cfgf)

def readConfig(cfile):
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    if 'External Commands' not in cfg.sections():
        print('Invalid Configuration')
        return False, False, False
    try:
        regf = cfg['External Commands']['registry-json']
        rloca = cfg['External Commands']['library-dir']
        cloca = cfg['External Commands']['compressed-dir']
    except KeyError:
        print('Invalid Configuration')
        return False, False, False
    if not regf or not rloca or not cloca:
        print('Invalid Configuration')
        return False, False, False
    return regf, rloca, cloca


