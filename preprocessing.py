from konlpy.tag import Okt
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# nltk 리소스 다운로드
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count+=1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count+=1
    return 1 if k_count>e_count else 0

# 텍스트 정의
text = "한국어 분석을 시작합니다. 재미있어요!"

if isEnglishOrKorean(text) == 1:

    # Okt 형태소 분석기 인스턴스 생성
    okt = Okt()

    # 형태소 분석 (토큰화)
    morphs = okt.morphs(text)
    print("형태소:", morphs)

    # 품사 태깅
    pos = okt.pos(text)
    print("품사 태깅:", pos)

    # 명사 추출
    nouns = okt.nouns(text)
    print("명사:", nouns)

elif isEnglishOrKorean(text) == 0:
    # 토큰화 (형태소 분석)
    tokens = word_tokenize(text)
    print("Tokens:", tokens)

    # 품사 태깅
    pos_tags = pos_tag(tokens)
    print("POS Tags:", pos_tags)

    # 명사 추출 (품사 태그가 NN, NNS, NNP, NNPS인 단어 추출)
    nouns = [word for word, pos in pos_tags if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
    print("Nouns:", nouns)
