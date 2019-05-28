import spacy

nlp = spacy.load("en_core_web_sm")
text = """
arpdog brown is a singer and harmonica player who has been active in canadas blues scene since 1982 hailing from vancouver he crossed tens of thousands of miles playing club dates and festivals in canada the northwestern united states and germanyover the years he has issued seven cds in 1995 his home is where the harp is won the muddy award for the best nw blues release from the cascade blues association in portland oregon as well that year it was nominated for a canadian juno for the best bluesgospel recording teamed up with graham guest on piano his cd naturally was voted 1 canadian blues album of 2010 by the blind lemon surveybrown tours extensively with his guitarist j arthur edmonds performing their electric mid1950s chicago blues either as a duo or with the full band while he is home he juggles a few combos working many venues big and small he also leads the harpdog brown band which is a gutsy traditional chicago blues band in 2014 they released what it is comprising mainly original songs and a few classic covers influential blues promoter and broadcaster holger petersen called what it is browns best albumhe was just awarded the maple blues award in toronto for best harmonica player in canada 2014 and was honored with a life time membership to the hamilton blues society
"""

initcap = text.title()
initcap
doc = nlp(text)
for token in doc:
    if token.pos_ == 'PROPN':
        print(token.text, token.pos_, token.dep_)

for ent in doc.ents:
    print(ent.text, ent.label_)
