import os

files = {}

for filename in os.listdir('C:\\Users\\Home\\Documents\\text'):
    if os.path.isfile(filename) \
       and f.endswith(".txt") \
       and not filename in files:
        with open(filename, "r") as file:
            files[filename] = file.read()

for filename, text in files.items():
    print(filename)
    # print("=" * 80)
    print(text)
    
