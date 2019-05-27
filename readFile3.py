import os

listResult = []

#PathFile = input('Input Path: ')
PathFile = "D:\\Python\\SRC\\Dev"
print(os.path.isdir(PathFile))
for filename in os.listdir(PathFile):
    if filename.endswith('.txt'):
        print('File Name : ' + filename)
        f = open(os.path.join(PathFile, filename), 'r', encoding='utf8')
        listResult.append([filename, f.read()])
print(listResult)
