import pickle
import json
from random import sample
lemma_file_path = r'preloaded\models\lemmatization\tamil_word_lemma.p'
input_file_path = r'sample_IO\main_sample_output.json'
fp = open(lemma_file_path, 'rb')

lemma_dict = pickle.load(fp)


def construct_sample_input(fp):
    null = None
    file = open(fp, 'r')
    input_data = json.load(file)
    sample_data = []
    for sent in input_data:
        for token in sent['Tokens']:
            sample_data.append([token['token'], token['Pos']])
    return sample_data

sample_input = construct_sample_input(input_file_path)


def lemmatize(word, pos):
  if word in lemma_dict:
    if pos in lemma_dict[word]:
      return lemma_dict[word][pos]
  return word

output_file_path = r'sample_IO\sample_lemma_output.json'
fp_o = open(output_file_path, 'w')
res = dict()

for word, pos in sample_input:
    res[word] = lemmatize(word, pos)
#   print("{} => {}".format(word, lemmatize(word, pos)))

# print(lemma_dict)

json.dump(res, fp_o, ensure_ascii=False, indent=4)
fp_o.close()