import os
import fnmatch

entries = os.listdir('C:\\Users\\Home\\Documents\\text')

for entry in entries:
    if fnmatch.fnmatch(entry, 'Table*.txt'):
        print(entry)


entries = os.scandir('C:\\Users\\Home\\Documents\\text')

with os.scandir('C:\\Users\\Home\\Documents\\text') as entries:
    for entry in entries:
        print(entry.name)
