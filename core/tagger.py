import pickle, re, os

from core.structures import Sentence

class AbstractTagger:
    def tag(sentence):
        pass

class TaggerWrapper:
    types = ['sklearn','keras']
    def __init__(self, tagger, type):
        self.type = type
        self.tagger = tagger

    def predict(self, feature_list):
        if self.type == "sklearn":
            return self.tagger.predict_single(feature_list)

class MLTagger(AbstractTagger):

    models_directory = r'preloaded\models\pos_tagging\\'
    models = {'ud_crf':('ud_crf_postagger_tamil.sav','sklearn')}

    def __init__(self, model = 'ud_crf'):
        self.model_name = model
        self.model = TaggerWrapper(pickle.load(open(self.models_directory+self.models[model][0], 'rb')), self.models[model][1])
        # self.model = TaggerWrapper(pickle.load(open('preloaded\models\pos_tagging\ud_crf_postagger_tamil.sav', 'rb')), self.models[model][1])

    def _extract_features(self, sentence, index):
            return {
                'word':sentence[index],
                'is_first':index==0,
                'is_last':index ==len(sentence)-1,
                'is_capitalized':sentence[index][0].upper() == sentence[index][0],
                'is_all_caps': sentence[index].upper() == sentence[index],
                'is_all_lower': sentence[index].lower() == sentence[index],
                'is_alphanumeric': int(bool((re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])',sentence[index])))),
                'prefix-1':sentence[index][0],
                'prefix-2':sentence[index][:2],
                'prefix-3':sentence[index][:3],
                'prefix-3':sentence[index][:4],
                'suffix-1':sentence[index][-1],
                'suffix-2':sentence[index][-2:],
                'suffix-3':sentence[index][-3:],
                'suffix-3':sentence[index][-4:],
                'prev_word':'' if index == 0 else sentence[index-1],
                'next_word':sentence[index+1] if index+1 < len(sentence) else '',
                'has_hyphen': '-' in sentence[index],
                'is_numeric': sentence[index].isdigit(),
                'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
                }

    def tag(self, sentence):
            input_sentence = sentence
            if not isinstance(sentence, Sentence):
                input_sentence = Sentence(0, len(sentence), sentence)
            reformed_sentence = [token.get() for token in input_sentence.tokens[1:-1]]
            features = [self._extract_features(reformed_sentence, idx) for idx in range(len(reformed_sentence))]
            tags = self.model.predict(features)
            # print(tags)
            for token_idx in range(1, len(input_sentence.tokens)-1):
                # print(input_sentence.tokens[token_idx], end=" ")
                input_sentence.tokens[token_idx].Pos = tags[token_idx-1]
            # print()
            
            return input_sentence
"""

# SAMPLE RUN 

t  = MLTagger()
res = t.tag("உடல் வலிமை பெற: அருகம்புல் சாறு, தேன் கலந்து சாப்பிட்டு வர ஊளை சதை குறையும். உடல் வலிமை பெறும்.")
for token in res:
    print(token, token.Pos, token.start_pos)
"""
