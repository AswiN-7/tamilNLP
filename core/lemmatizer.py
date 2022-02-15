import pickle, os, json

class AbstractLemmatizer:
    def lemmatize():
        pass

class DictionaryLemmatizer(AbstractLemmatizer):

    dict_directory = r'preloaded\models\lemmatization\tamil_word_lemma.p'

    def __init__(self):
        self.lemma_dict = pickle.load(open(self.dict_directory,'rb'))

    def lemmatize(self, word, pos):
        if word is None:
            return ''
        if pos is None:
            pos = ''
        # word = str(word).lower()
        # pos = str(pos).upper()
        if word in self.lemma_dict:
            if pos in self.lemma_dict[word]:
                return self.lemma_dict[word][pos]
        return word

"""
# SAMPLE RUN CHECK

input_file_path = r'sample_IO\main_sample_output.json'
output_file_path = r'sample_IO\sample_lemma_output.json'


def construct_sample_input(fp):
    null = None
    file = open(fp, 'r')
    input_data = json.load(file)
    sample_data = []
    for sent in input_data:
        for token in sent['Tokens']:
            sample_data.append([token['token'], token['Pos']])
    return sample_data




l = DictionaryLemmatizer()



sample_input = construct_sample_input(input_file_path)

fp_o = open(output_file_path, 'w')
result = dict()

for word, pos in sample_input:
    print(word)
    res = l.lemmatize(word,pos)
    result[word]= res

json.dump(result, fp_o, ensure_ascii=False, indent=4)
fp_o.close()

"""