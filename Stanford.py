from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize
import os
from nltk.corpus import stopwords
import csv

def stopw(document):
    stop = stopwords.words('english')
    res = ' '.join([i for i in document.split() if i not in stop])
    return res

text = """
harpdog brown is a singer and harmonica player who has been active in canadas blues scene since 1982 hailing from vancouver he crossed tens of thousands of miles playing club dates and festivals in canada the northwestern united states and germanyover the years he has issued seven cds in 1995 his home is where the harp is won the muddy award for the best nw blues release from the cascade blues association in portland oregon as well that year it was nominated for a canadian juno for the best bluesgospel recording teamed up with graham guest on piano his cd naturally was voted 1 canadian blues album of 2010 by the blind lemon surveybrown tours extensively with his guitarist j arthur edmonds performing their electric mid1950s chicago blues either as a duo or with the full band while he is home he juggles a few combos working many venues big and small he also leads the harpdog brown band which is a gutsy traditional chicago blues band in 2014 they released what it is comprising mainly original songs and a few classic covers influential blues promoter and broadcaster holger petersen called what it is browns best albumhe was just awarded the maple blues award in toronto for best harmonica player in canada 2014 and was honored with a life time membership to the hamilton blues society
"""

# Add the jar and model via their path (instead of setting environment variables):
jar = 'D:\\Python\\SRC\\stanford-postagger-full-2018-10-16\\stanford-postagger.jar'

model = 'D:\\Python\\SRC\\stanford-postagger-full-2018-10-16\\models\\english-left3words-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

clean = stopw(text)
text = pos_tagger.tag(word_tokenize(clean))
print(text)

st = StanfordNERTagger('D:\\Python\\SRC\\stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz',
					   'D:\\Python\\SRC\\stanford-ner-2018-10-16\\stanford-ner.jar',
					   encoding='utf-8')

initText = clean.title()
tokenized_text = word_tokenize(initText)
tokenized_text
classified_text = st.tag(tokenized_text)
classified_text


listwho = []
f = open(os.path.join('D:\\Python\\SRC\\Dev', '29.txt'), 'r', encoding='utf8')
plain = f.read()
cln = stopw(plain)
tokenized_text = word_tokenize(cln.title())
classified_text = st.tag(tokenized_text)
# classified_text
for x in classified_text:
	if x[1] == 'PERSON':
		listwho.extend([x[0]])

listwho

path = 'D:\\Python\\SRC'
header = [['id', 'pii']]
with open(os.path.join(path, 'result.csv'), 'w') as csvFile:
    csvFile.write('id,pii\n')
    for p in listwho:
        try:
            csvFile.write('{},"{}"\n'.format(p[0], json.dumps(p[1]).replace('"', '""')))
        except:
            pass
for p in listwho:
    print(p[0])
