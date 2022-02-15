from structures import *
inp_file = open(r'dataset\sample\general-1.txt', 'r')
text = inp_file.read()

nlp = Document(text)

filePath = "dataset\sample\smaple_tokenization_output.txt"
fp = open(filePath, 'w', encoding='utf-8')

for sent in nlp:
  fp.write("{} {} {}\n\t".format(sent.get(), str(sent.start_pos), str(sent.end_pos)))
  for to in sent:
    fp.write("{} {} {}  ".format(to.get(), str(to.start_pos), str(to.end_pos)))
  fp.write("\n")
fp.close()
# for sent in nlp:
  # print(sent)
"""
SAMPLE I/O 
present in dataset\sample\smaple_tokenization_output.txt
"""
