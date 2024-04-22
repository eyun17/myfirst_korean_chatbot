from utils.Preprocessing import Preprocess


sent = "내일 오전 10시에 탕수육 주문하고 싶어"

# Preprocessing 객체 생성
p = Preprocess(userdic='./user_dic.tsv')

# pos 메서드를 통해 형태소 분석 수행
pos = p.pos(sent)

# 품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret)

# 품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret)
