import os
import nltk
from nltk.corpus import stopwords
from dateparser.search import search_dates


def stopw(str):
    str = ' '.join([word for word in str.split() if word not in stopwords.words("english")])
    return str


def scrubDate(list):
    rdate = search_dates(list)
    need = [result for result in rdate if result[0].lower() != "today"]
    for x in need:
        xdate = x[0]


# ----------------------------- Main --------------------------------
listResult = []
#PathFile = input('Input Path: ')
# stop = stopwords.words('english')
# res = ' '.join([i for i in document.split() if i not in stop])

path = 'D:\\Python\\SRC\\Dev'
for filename in os.listdir(path):
    if filename.endswith('.txt'):
        # print('File Name : ' + filename)
        f = open(os.path.join(PathFile, filename), 'r', encoding='utf8')
        tokenized_text = word_tokenize(f.read())
        
tokenized_text






#         listResult.append([filename, f.read()])
#
# listResult
