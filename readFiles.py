import os
import fnmatch

import fileinput
import sys


entries = os.listdir('C:\\Users\\Home\\Documents\\text')

for entry in entries:
    if fnmatch.fnmatch(entry, 'Table*.txt'):
        print(entry)

for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()


# alternative listdir using scandir
with os.scandir('C:\\Users\\Home\\Documents\\text') as entries:
    for entry in entries:
        print(entry.name)
