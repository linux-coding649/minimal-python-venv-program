# Created by linux649 under the GNU GPLv3 License

# VEP (Virtual Environment Program) Downloader Copyright (C) 2023  linux649
# This program comes with ABSOLUTELY NO WARRANTY; for details go to <https://www.gnu.org/licenses>'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; go to <https://www.gnu.org/licenses> for details.

from sys import exit
import urllib.request
import urllib.error

print('VEP Downloader Program')
ver = input('VEP semantic version: ')
try:
    urllib.request.urlretrieve(f'https://github.com/linux-coding649/minimal-python-venv-program/archive/refs/tags/v{ver}.zip',
                                f'VEP-download-{ver}.zip')
    print(f'The file has been successfully downloaded at VEP-download-{ver}.zip')
except urllib.error.HTTPError:
    print('Invalid version, not downloading')
    exit(1)
exit(0)