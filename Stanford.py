from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize

# Add the jar and model via their path (instead of setting environment variables):
jar = 'D:\\Python\\SRC\\stanford-postagger-full-2018-10-16\\stanford-postagger.jar'

model = 'D:\\Python\\SRC\\stanford-postagger-full-2018-10-16\\models\\english-left3words-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

text = pos_tagger.tag(word_tokenize("What's the airspeed of an unladen swallow by smith cullens?"))
print(text)

st = StanfordNERTagger('D:\\Python\\SRC\\stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz',
					   'D:\\Python\\SRC\\stanford-ner-2018-10-16\\stanford-ner.jar',
					   encoding='utf-8')

text = 'While in France, josef smith discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)
