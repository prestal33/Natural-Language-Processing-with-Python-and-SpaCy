import spacy
from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('en_core_web_sm')
nlp.get_pipe( 'attribute_ruler' ).add( patterns=[[{ 'ORTH': 'Frisco' }]], attrs={ 'LEMMA': 'San Francisco' }) 
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')

print([w.text for w in doc if w.tag_=='VBG' or w.tag_=='VB'])
print([w.text for w in doc if w.pos_=='PROPN'])



'''nlp.tokenizer.add_special_case(u'Frisco', special_case) 
    ^^^ does not work in spacy v3; they may add it back in next update; above is workaround'''
#print([w.lemma_ for w in doc])

for token in doc: #part of speech
    print(token.text, token.lemma_, token.pos_, token.dep_, token.tag_)

'''for token in doc: #head of part of speech
    print(token.head.text, token.pos_, token.dep_)'''

print('Actual Results Below')
for sent in doc.sents:
    print([w.lemma_ for w in sent if (w.dep_ == 'ROOT' and w.tag_!='VBN') or (w.dep_ == 'pobj' and w.pos_=='PROPN')]) 