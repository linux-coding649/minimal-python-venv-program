import json
import importlib

def loadRegistry(rfile, extCmdDir):
    retval = 1
    try:
        with open(rfile, 'r') as loadFile:
            raw = loadFile.read()
            loadFile.close()
        jsonRegistryDB = json.loads(raw)
        for i in jsonRegistryDB["registered-libraries"]:
            try:
                importlib.import_module(f'{extCmdDir}.{i}')
                print(f'Successfully found command library [{i}]')
            except ImportError:
                print(f'External Commands Import Failed: Unable to Import {i}')
                print("Failed to Import External Commands, Rolling Back to ONLY BuiltIns")
                return 1
        retval = jsonRegistryDB["registered-libraries"]
    except FileNotFoundError:
        print(f"No Registry File Such As {rfile}")
    except json.JSONDecodeError:
        print("Unsupported File Format, Rolling Back To ONLY BuiltIns")
    except KeyError:
        print("Unsupported File Format, Rolling Back To ONLY BuiltIns")
    return retval

def createRegistry(rfile):
    with open(rfile, 'w') as loadFile:
        loadFile.truncate(0)
        loadFile.write(json.dumps({'registered-libraries':[]}))
        loadFile.close()