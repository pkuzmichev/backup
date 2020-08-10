import os
import sys
import time
import zipfile
from datetime import datetime


def backup():
    path = sys.argv[1]
    print('backup path:', path)

    archive(path)


def name():
    name_archive = time.ctime().replace(' ', '_') + '.zip'
    print('archive name:', name_archive)
    return name_archive


def archive(path):
    start_time = datetime.now()
    arch = zipfile.ZipFile(name(), 'w', compression=zipfile.ZIP_LZMA)
    for root, dirs, files in os.walk(path):
        for file in files:
            arch.write(os.path.join(root, file))
            print(file)
    arch.close()
    print('time:', datetime.now() - start_time)


if __name__ == '__main__':
    backup()
