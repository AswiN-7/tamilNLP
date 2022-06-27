import encodings
import pickle
import re
import json
modelFilePath = r'preloaded\models\pos_tagging\ud_crf_postagger_tamil.sav'
fp = open(modelFilePath, 'rb')
outputFilePath = r'sample_IO\sample_tagging_output.json'

pos_model = pickle.load(fp)

def extract_features(sentence, index):
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

sent = "உடல் வலிமை பெற: அருகம்புல் சாறு, தேன் கலந்து சாப்பிட்டு வர ஊளை சதை குறையும். உடல் வலிமை பெறும்."

features = [extract_features(sent.split(), idx) for idx in range(len(sent.split()))]
# print(features)
res = pos_model.predict_single(features)
print(res)

res_out = []
for word, pos in zip(sent.split(), res):
    res_out.append((word, pos))
fp = open(outputFilePath, 'w')
json.dump(res_out, fp, ensure_ascii=False, indent=4)
fp.close()