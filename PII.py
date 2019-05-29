import spacy

def getPII(content):
    PII = []
    doc = nlp(content)
    for dt in doc.ents:
        PII.append([dt.text, dt.label_])

    return PII

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
