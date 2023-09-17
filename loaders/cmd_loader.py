# Created by linux649 under the GNU GPLv3 License

# VEP (Virtual Environment Program) External Command Programs Loader  Copyright (C) 2023  linux649
# This program comes with ABSOLUTELY NO WARRANTY; for details go to <https://www.gnu.org/licenses>'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; go to <https://www.gnu.org/licenses> for details.

import json
import importlib
import gzip
import sys

def loadRegistry(rfile, extCmdDir, cmpCmdDir):
    retval = 1
    ltd = []
    extCmdDirPath = extCmdDir.replace('.', '/')+'/' if sys.platform == 'linux' else extCmdDir.replace('.', '\\')+'\\'
    cmpCmdDirPath = cmpCmdDir.replace('.', '/')+'/' if sys.platform == 'linux' else cmpCmdDir.replace('.', '\\')+'\\'
    try:
        with open(rfile, 'r') as loadFile:
            raw = loadFile.read()
            loadFile.close()
        jsonRegistryDB = json.loads(raw)
        for i in jsonRegistryDB['registered-compressed']:
            try:
                with gzip.open(cmpCmdDirPath+i+'.py.gz', 'r') as gzf:
                    cnttd = gzf.read().decode()
                    gzf.close()
                    ltd.append(extCmdDirPath+i+'.py')
                with open(extCmdDirPath+i+'.py', 'x') as ftwt:
                    ftwt.write(cnttd)
                    ftwt.close()
            except FileNotFoundError:
                print('Unable to read and decompress compressed .gz libraries')
                print('Skipping nonexistent library...')
                continue
            except FileExistsError:
                print('Unexpected file interrupted decompression, decompression failed')
                print('Skipping this compressed library...')
                continue
            else:
                jsonRegistryDB['registered-libraries'].append(i)
                continue
        for i in jsonRegistryDB["registered-libraries"]:
            try:
                importlib.import_module(f'{extCmdDir}.{i}')
                print(f'Successfully found command library [{i}]')
            except ImportError:
                print(f'External Commands Import Failed: Unable to Import {i}')
                print("Failed to Import External Commands, Rolling Back to ONLY BuiltIns")
                return 1, None
        retval = jsonRegistryDB["registered-libraries"]
    except FileNotFoundError:
        print(f"No Registry File Such As {rfile}")
    except json.JSONDecodeError:
        print("Unsupported File Format, Rolling Back To ONLY BuiltIns")
    except KeyError:
        print("Unsupported File Format, Rolling Back To ONLY BuiltIns")
    return retval, ltd

def createRegistry(rfile):
    with open(rfile, 'w') as loadFile:
        loadFile.truncate(0)
        loadFile.write(json.dumps({'registered-libraries':[], 'registered-compressed':[]}))
        loadFile.close()
