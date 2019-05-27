import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion by Yusuf Fachruddin")
for token in doc:
    if token.pos_ == 'PROPN':
        print(token.text, token.pos_, token.dep_)

for ent in doc.ents:
    print(ent.text, ent.label_)
    
