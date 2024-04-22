#
# 챗봇에서 사용하는 사전 파일 생성
#

from utils.Preprocessing import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # splitlines(): 문자열을 라인 단위로 분리하여 리스트로 반환
        # data: [['안녕하세요.', '0'], ['반가워요.', '0'], ...]
        # remove header
        data = data[1:]
    return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('./corpus.txt')

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    # c[0]: 문장, c[1]: 레이블
    pos = p.pos(c[0])
    # k is a keyword
    for k in p.get_keywords(pos, without_tag=True):
        dict.append(k)

# 사전에 사용될 word2index 생성
# 사전의 첫 번째 인덱스에는 OOV 사용 : OOV (Out Of Vocabulary): 사전에 없는 단어
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
# fit_on_texts: 사전을 만들기 위해 데이터를 입력으로 받음
tokenizer.fit_on_texts(dict)
# word_index: 단어와 인덱스의 쌍을 가지는 딕셔너리
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()