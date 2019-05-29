import os

#yu Natural Language Understanding
class NLPyu:
    def __init__(self, path=None):
        self.path = [] if path is None else path

    def getContent(self):
        listResult = []
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                f = open(os.path.join(PathFile, filename), 'r', encoding='utf8')
                listResult.append([filename, f.read()])
        return listResult
