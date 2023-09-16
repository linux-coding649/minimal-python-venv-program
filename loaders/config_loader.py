import configparser

def createConfig(cfile):
    cfg = configparser.ConfigParser()
    cfg['External Commands'] = {'registry-json':'registry.external.json',
                                'library-dir': 'loaders.extCmds'}
    with open(cfile, 'w') as cfgf:
        cfg.write(cfgf)

def readConfig(cfile):
    cfg = configparser.ConfigParser()
    cfg.read(cfile)
    if 'External Commands' not in cfg.sections():
        print('Invalid Configuration')
        return False, False
    try:
        regf = cfg['External Commands']['registry-json']
        rloca = cfg['External Commands']['library-dir']
    except KeyError:
        print('Invalid Configuration')
        return False, False
    if not regf or not rloca:
        print('Invalid Configuration')
        return False, False
    return regf, rloca


