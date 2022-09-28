import spacy 

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])