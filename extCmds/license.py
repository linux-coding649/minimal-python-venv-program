LOADER_CMD_HELP = '''commands:
          help                 | Shows this help menu
          ?                    | Shows this help menu
          lcns                 | Shows the license
          wrnt                 | Shows the warranty'''

def __command__(cmd):
    global LOADER_CMD_HELP
    if cmd == 'help':
        print(LOADER_CMD_HELP)
    elif cmd == 'lcns':
        print('''VEP (Virtual Environment Program)  Copyright (C) 2023  linux649
This program comes with ABSOLUTELY NO WARRANTY; for details type `wrnt'.
This is free software, and you are welcome to redistribute it
under certain conditions; go to <https://www.gnu.org/licenses> for details.''')
    elif cmd == 'wrnt':
        print('''THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.''')
    else:
        return True