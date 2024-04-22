from konlpy.tag import Komoran

class Preprocess:
    def __init__(self, userdic=None): # this is the constructor
        # initialize the morpheme analizer
        self.komoran = Komoran(userdic=userdic)
        # userdic 인자에 사용자 정의 사전 파일의 경로 입력 가능

        # define postags to be excluded
        # 관계언 제거, 기호 제거
        # 어미 제거
        # 접미사 제거
        # 불용어로 정의된 태그들은 핵심 키워드에서 제외
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ',
            'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    # 형태소 분석기 POS TAGGER
    # 클래스 외부에서 코모란 형태소 분석기 객체를 직접적으로 호출할 일이 없게 하기 위해 정의한 wrapper function
    # 형태소 분석기 변경할 경우 이 래퍼 함수 내용으로만 변경하면 됌.
    def pos(self, sentence):
        return self.komoran.pos(sentence)

    # Retrieve only necessary part-of-speech information after removing stop words
    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags # f is a lambda function that returns True if x is in self.exclusion_tags
        word_list = []
        for p in pos:
            # if the part-of-speech information is not in the exclusion_tags
            if f(p[1]) is False:
                # append the part-of-speech information if without_tag is False, otherwise append the word
                word_list.append(p if without_tag is False else p[0])
            return word_list


