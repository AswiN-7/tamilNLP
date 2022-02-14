
"""
procedure
map tamil characters to tanglish charaters and form a dictionary

maximum a character length can go to 5 
  so parsing the input string length 5 if the length of the string graeter then 5 every time

  if these parsed set of characters are collectively represented as a single charater in hashmap then add the dest lang character to output string and remove this charater from input string 
  continue this input string become empty

"""


tamil = [
      "அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஒள","ஃ",
      "க","கா","கி","கீ","கு","கூ","கெ","கே","கை","கொ","கோ","கௌ","க்" ,
      "ங","ஙா","ஙி","ஙீ","ஙு","ஙூ","ஙெ","ஙே","ஙை","ஙொ","ஙோ","ஙௌ","ங்",
      "ச","சா","சி","சீ","சு","சூ","செ","சே","சை","சொ","சோ","சௌ","ச்",
      "ஞ","ஞா","ஞி","ஞீ","ஞு","ஞூ","ஞெ","ஞே","ஞை","ஞொ","ஞோ","ஞௌ","ஞ்",
      "ட","டா","டி","டீ","டு","டூ","டெ","டே","டை","டொ","டோ","டௌ","ட்" ,
      "ண","ணா","ணி","ணீ","ணு","ணூ","ணெ","ணே","ணை","ணொ","ணோ","ணௌ","ண்" ,
      "த","தா","தி","தீ","து","தூ","தெ","தே","தை","தொ","தோ","தௌ","த்" ,
      "ந","நா","நி","நீ","நு","நூ","நெ","நே","நை","நொ","நோ","நௌ","ந்",
      "ப","பா","பி","பீ","பு","பூ","பெ","பே","பை","பொ","போ","பௌ","ப்",
      "ம","மா","மி","மீ","மு","மூ","மெ","மே","மை","மொ","மோ","மௌ","ம்" ,
      "ய","யா","யி","யீ","யு","யூ","யெ","யே","யை","யொ","யோ","யௌ","ய்",
      "ர","ரா","ரி","ரீ","ரு","ரூ","ரெ","ரே","ரை","ரொ","ரோ","ரௌ","ர்",
      "ல","லா","லி","லீ","லு","லூ","லெ","லே","லை","லொ","லோ","லௌ","ல்" ,
      "வ","வா","வி","வீ","வு","வூ","வெ","வே","வை","வொ","வோ","வெள","வ்" ,
      "ழ","ழா","ழி","ழீ","ழு","ழூ","ழெ","ழே","ழை","ழொ","ழோ","ழெள","ழ்",
      "ள","ளா","ளி","ளீ","ளு","ளூ","ளெ","ளே","ளை","ளொ","ளோ","ளௌ","ள்" ,
      "ற","றா","றி","றீ","று","றூ","றெ","றே","றை","றொ","றோ","றெள","ற்" ,
      "ன","னா","னி","னீ","னு","னூ","னெ","னே","னை","னொ","னோ","னௌ","ன்" ,
      "ஷ","ஷா","ஷி","ஷீ","ஷு","ஷூ","ஷெ","ஷே","ஷை","ஷொ","ஷோ","ஷௌ","ஷ்",
      "ஸ","ஸா","ஸி","ஸீ","ஸு","ஸூ","ஸெ","ஸே","ஸை","ஸொ","ஸோ","ஸௌ","ஸ்",
      "ஜ","ஜா","ஜி","ஜீ","ஜு","ஜூ","ஜெ","ஜே","ஜை","ஜொ","ஜோ","ஜௌ","ஜ்" ,
      "ஹ","ஹா","ஹி","ஹீ","ஹு","ஹூ","ஹெ","ஹே","ஹை","ஹொ","ஹோ","ஹௌ","ஹ்",
      "க்ஷ","க்ஷா","க்ஷி","க்ஷீ","க்ஷு","க்ஷூ","க்ஷெ","க்ஷே","க்ஷை","க்ஷொ","க்ஷோ","க்ஷெள","க்ஷ்",
      "ஸ்ரீ"]


tanglish = ["a","aa","i","ii","u","uu","e","ee","ai","o","oo","au","q",
        "ka","kaa","ki","kii","ku","kuu","ke","kee","kai","ko","koo","kau","k",
        "nga","ngaa","ngi","ngii","ngu","nguu","nge","ngee","ngai","ngo","ngoo","ngau","ng",
        "ca","caa","ci","cii","cu","cuu","ce","cee","cai","co","coo","cau","c",
        "nja","njaa","nji","njii","nju","njuu","nje","njee","njai","njo","njoo","njau","nj",
        "Ta","Taa","Ti","Tii","Tu","Tuu","Te","Tee","Tai","To","Too","Tau","T",
        "Na","Naa","Ni","Nii","Nu","Nuu","Ne","Nee","Nai","No","Noo","Nau","N",
        "ta","taa","ti","tii","tu","tuu","te","tee","tai","to","too","tau","t",
        "nda","ndaa","ndi","ndii","ndu","nduu","nde","ndee","ndai","ndo","ndoo","ndau","nd",
        "pa","paa","pi","pii","pu","puu","pe","pee","pai","po","poo","pau","p",
        "ma","maa","mi","mii","mu","muu","me","mee","mai","mo","moo","mau","m",
        "ya","yaa","yi","yii","yu","yuu","ye","yee","yai","yo","yoo","yau","y",
        "ra","raa","ri","rii","ru","ruu","re","ree","rai","ro","roo","rau","r",
        "la","laa","li","lii","lu","luu","le","lee","lai","lo","loo","lau","l",
        "va","vaa","vi","vii","vu","vuu","ve","vee","vai","vo","voo","vau","v",
        "zha","zhaa","zhi","zhii","zhu","zhuu","zhe","zhee","zhai","zho","zhoo","zhau","zh",
        "La","Laa","Li","Lii","Lu","Luu","Le","Lee","Lai","Lo","Loo","Lau","L",
        "Ra","Raa","Ri","Rii","Ru","Ruu","Re","Ree","Rai","Ro","Roo","Rau","R",
        "na","naa","ni","nii","nu","nuu","ne","nee","nai","no","noo","nau","n",
        "Sha","Shaa","Shi","Shii","Shu","Shuu","She","Shee","Shai","Sho","Shoo","Shau","Sh",
        "sa","saa","si","sii","su","suu","se","see","sai","so","soo","sau","s",
        "ja","jaa","ji","jii","ju","juu","je","jee","jai","jo","joo","jau","j",
        "ha","haa","hi","hii","hu","huu","he","hee","hai","ho","hoo","hau","h",
        "xa","xA","xi","xii","xu","xuu","xe","xee","xai","xo","xoo","xau","x",
        "Sra"
]

# print(len(tamil), len(tanglish))
tang_to_ta = dict()

def mapping(x_table, y_table, map):
  for k, v in zip(x_table, y_table):
    map[k] = v
  # print(map)

mapping(tanglish, tamil, tang_to_ta)
# tang_to_ta
map = tang_to_ta
def convert_tang_to_tamil(inp_str):
  global map
#   inp_cp = "" #debug
  out_str = ""
  while inp_str:
    length = len(inp_str)
    if length >5:
      length = 5
    parse = length    
    while parse > 0:
      parsed_char = inp_str[:parse]
      if parsed_char in map:
        out_str += map[parsed_char]
        # inp_cp += inp_str[:parse]  # just to visualize
        inp_str = inp_str[parse:]
        # print(inp_cp, " : ", out_str) #debug
        break
      parse-=1
    
    if parse == 0:
      # if no char is matched then add that char to output and move
      out_str += inp_str[0]
      inp_str = inp_str[1:]
  return out_str

filePath = "dataset\sample\smaple_tang_to_ta_output.txt"
fp = open(filePath, 'w', encoding='utf-8')

tanglish_words = ["makaatmaakkaLuL", "makaatmaavinatu", "makaatmaakkaLaaka", "makaatmaavinuTaiya", "makaatmaaviRkee", "makaatmaaviTamum", "makaatmaavai", "makaatmaataan", "makaatmaavukku", "makaatmaaviTam", "makaatmaavum", "makaatmaakkaL", "makaatmaavaip", "makaatmaakaandtiyaip", "makaatmaavaippaRRi", "makaatmaavin", "makaatmaa", "makaatmaakaandti"]
for word in tanglish_words:
    tamil_word = convert_tang_to_tamil(word)
    fp.write("{} => {}\n".format(word, tamil_word))

fp.close()

"""
SAMPLE I/O
present in dataset\sample\smaple_tang_to_ta_output.txt
"""