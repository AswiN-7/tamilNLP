import sys
from textwrap import indent

from matplotlib.font_manager import json_dump
from core.structures import Document
from core.tagger import MLTagger
import json


def process(raw_document, pipeline = ['sentencize','pos']):
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
    return document

s= process("உடல் வலிமை பெற: அருகம்புல் சாறு, தேன் கலந்து சாப்பிட்டு வர ஊளை சதை குறையும். உடல் வலிமை பெறும்.")

filePath = r'dataset\sample\main_sample_output.json'
res = []
fp = open(filePath, 'a')

for sent in s:
    new_s = dict()
    new_s['sentence'] = sent.get()
    new_s['Tokens'] = []
    for word in sent:
        new_t = dict()
        new_t['token'] = word.get()
        new_t['Pos'] = word.Pos
        new_t['lemma'] = word.repr
        new_s['Tokens'].append(new_t)
    res.append(new_s)
json.dump(res, fp, ensure_ascii=False, indent= 4)
fp.close()