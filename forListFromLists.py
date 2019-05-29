import os

dir = "D:\\Python\\SRC\\Dev"
for filename in os.listdir(dir):
    if filename.endswith('.txt'):
        # print('File Name : ' + filename)
        f = open(os.path.join(dir, filename), 'r', encoding='utf8')
        plain = f.read()

plain
