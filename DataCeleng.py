import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from dateparser.search import search_dates





def getCC(string):
    # pattern = r"(^|\s+)(\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4})(?:\s+|$)"
    # pattern = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    pattern = r"([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$"
    match = re.search(pattern, string)

    if match:
        print(match.group(0))

def getPhone(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def getEmail(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def sw(document):
    stop = stopwords.words('english')
    res = ' '.join([i for i in document.split() if i not in stop])
    return res

def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

st = StanfordNERTagger('D:\\Python\\SRC\\stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz',
					   'D:\\Python\\SRC\\stanford-ner-2018-10-16\\stanford-ner.jar',
					   encoding='utf-8')

def scrubbing(path):
    listResult = []
    #PathFile = input('Input Path: ')
    PathFile = path
    print(os.path.isdir(PathFile))
    for filename in os.listdir(PathFile):
        if filename.endswith('.txt'):
            # print('File Name : ' + filename)
            f = open(os.path.join(PathFile, filename), 'r', encoding='utf8')
            plain = sw(f.read())

            # crop expected date
            rdate = search_dates(plain)
            need = [result for result in rdate if result[0].lower() != "today"]
            for x in need:
                xdate = x[0]

            tokenized_text = word_tokenize(plain)
            classified_text = st.tag(tokenized_text)
            for x in classified_text:
                name = x[0]

            # aemail = getEmail(plain)
            # for y in aemail:
            #     email = y[0]

            listResult.append([filename.replace(".txt", ""), name, xdate])
    return listResult


result = scrubbing('D:\\Python\\SRC\\Dev')
result


# plain
#
# header = [['id', 'pii']]
# with open(os.path.join(OutFile, 'D:\\Python\\SRC\\train_labelsx.csv'), 'w') as csvFile:
#     csvFile.write('id,pii\n')
#     for p in listResult:
#         try:
#             csvFile.write('{},"{}"\n'.format(p[0], json.dumps(p[1]).replace('"', '""')))
#         except:
#             pass
