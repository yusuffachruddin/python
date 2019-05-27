import os

files = {}

for filename in os.listdir('D:\\Python\\SRC\\Dev'):
    if os.path.isfile(filename) \
       and f.endswith(".txt") \
       and not filename in files:
        with open(filename, "r") as file:
            files[filename] = file.read()

for filename, text in files.items():
    print(filename)
    # print("=" * 80)
    print(text)

print(filename)
