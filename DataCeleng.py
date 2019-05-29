import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize
import json
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from dateparser.search import search_dates


def stopw(document):
    stop = stopwords.words('english')
    res = ' '.join([i for i in document.split() if i not in stop])
    return res


def getCC(path, filename):
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    strRe = r'^(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11}'
    # r = re.compile(r'([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$')
    r = re.compile(strRe)
    # convert to set to distinct value then convert back to list
    # return list(set(r.findall(plain)))
    return r.findall(plain)

def getValidCC(path, filename):
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    ccard = re.findall(r'''4\d{12}\d{3}?|
                    5[1-5]\d{4}\d{10}|
                    677189\d{10}|
                    30[0-5]\d{11}|
                    3[68]\d\d{11}|
                    3[47]\d{13}|
                    6011\d{12}|
                    65\d{2}\d{12}
                    ''', plain, re.X)
    return list(set(ccard))

def getPhone(path, filename):
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(plain)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def getEmail(path, filename):
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    # p = re.compile(r'([^<]+)<[^<]*>(?:;\s*)?')
    r = re.compile(r'[\sa-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    # convert to set to distinct value then convert back to list
    # return list(set(r.findall(plain)))
    return  r.findall(plain)

def stopw(document):
    stop = stopwords.words('english')
    res = ' '.join([i for i in document.split() if i not in stop])
    return res


def nltkstanf(path, filename):
    st = StanfordNERTagger('D:\\Python\\SRC\\stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz',
    					   'D:\\Python\\SRC\\stanford-ner-2018-10-16\\stanford-ner.jar',encoding='utf-8')
    listwho = []
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    cln = stopw(plain)
    tokenized_text = word_tokenize(cln.title())
    classified_text = st.tag(tokenized_text)
    # classified_text
    for x in classified_text:
    	if x[1] == 'PERSON':
    		listwho.extend([x[0]])
    return listwho

def getDates(path, filename):
    listdt = []
    f = open(os.path.join(path, filename), 'r', encoding='utf8')
    plain = f.read()
    cln = stopw(plain)
    results = search_dates(cln)
    # exclude results matching to “today”
    need = [result for result in results if result[0].lower() != "today"]

    for x in need:
    	listdt.extend([x[0]])

    return listdt


listResult = []
#PathFile = input('Input Path: ')
path = 'D:\\Python\\SRC\\Dev'
print(os.path.isdir(path))
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        # grab name from each file
        lstEmail = []
        lstwho = []
        lstDT = []
        lstCC = []
        lstPhon = []
        lstEmail = getEmail(path,filename)
        lstwho = nltkstanf(path,filename)
        lstDT = getDates(path,filename)
        lstCC = getValidCC(path,filename)
        # lstPhon = getPhone(path, filename)
# lstEmail + lstwho + lstDT + lstCC
        listResult.append([filename.replace(".txt", ""),lstEmail])


listResult


# getPhone(path, filename)
# getValidCC(path, filename)
# plain
#

header = [['id', 'pii']]
with open('D:\\Python\\SRC\\train_labelsx.csv', 'w') as csvFile:
    csvFile.write('id,pii\n')
    for p in listResult:
        # try:
            if p[1]!=[]:
                csvFile.write('{},"{}"\n'.format(p[0], json.dumps(p[1]).replace('"', '""')))
            else:
                csvFile.write('{},{}\n'.format(p[0], json.dumps(p[1]).replace('"', '""')))
        # except:
        #     pass
