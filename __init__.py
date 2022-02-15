import sys
from core.structures import Document
from core.tagger import MLTagger
from core.lemmatizer import DictionaryLemmatizer

import json


def process(raw_document, pipeline = ['sentencize','pos','lemmatization']):
    document = raw_document
    if 'sentencize' in pipeline:
        document = Document(document)
    if 'pos' in pipeline:
        tagger = MLTagger()
        if isinstance(document, Document):
            sentences = [tagger.tag(sentence) for sentence in document]
            # document.sentences = sentences
        else:
            document = tagger.tag(document)
    if 'lemmatization' in pipeline:
        lemmatizer = DictionaryLemmatizer()
        if isinstance(document, Document):
            for sentence in document:
                for token in sentence:
                    token.repr = lemmatizer.lemmatize(token.raw, token.Pos)
                # for token_index in range(len(sentence.tokens)):
                #     sentence[token_index].repr = lemmatizer.lemmatize(sentence[token_index].get(), sentence[token_index].Pos)

    return document


text = "உடல் வலிமை பெற: அருகம்புல் சாறு, தேன் கலந்து சாப்பிட்டு வர ஊளை சதை குறையும். உடல் வலிமை பெறும்."
pipeline = ['sentencize','pos','lemmatization']
s= process(text, pipeline=pipeline)

filePath = r'sample_IO\main_sample_output.json'
res = []
fp = open(filePath, 'w')

for sent in s:
    new_s = dict()
    new_s['sentence'] = sent.get()
    new_s['Tokens'] = []
    for word in sent:
        new_t = dict()
        new_t['token'] = word.raw
        new_t['Pos'] = word.Pos
        new_t['lemma'] = word.repr
        new_s['Tokens'].append(new_t)
    res.append(new_s)
json.dump(res, fp, ensure_ascii=False, indent= 4)
fp.close()