import spacy
from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'this product both integrates both libraries for downloading and applying patches')
doc2 = nlp(u'I am flying to Frisco.')

for token in doc:
    print(token.text, token.lemma_)

print([w.text for w in doc])

#special case
special_case = [{ ORTH: u'Frisco', LEMMA: u'San Francisco' }]
nlp.get_pipe( 'attribute_ruler' ).add( [[{ 'TEXT': 'Frisco' }]], { 'LEMMA': 'San Francisco' }) 
'''nlp.tokenizer.add_special_case(u'Frisco', special_case) 
    ^^^ does not work in spacy v3; they may add it back in next update; above is workaround'''
print([w.lemma_ for w in nlp(u'I am flying to Frisco.')])
