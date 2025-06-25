# 대표적인 한국어 불용어 리스트
korean_stopwords = ["은", "는", "이", "가", "에", "을", "를", "도", "와", "과", "한", "하다"]

sentence = "나는 오늘 학교에 갔어요."

import re

def tokenize_korean(text):
    # 문장부호 분리
    text = re.sub(r'([.,!?])', r' \1 ', text)
    # 대표적인 조사 분리
    particles = ['은', '는', '이', '가', '에', '을', '를', '도', '와', '과']
    for p in particles:
        text = re.sub(r'(.+?)' + p + r'\b', r'\1 ' + p, text)
    # 공백 기준 분리
    return text.split()

# 토큰화
tokens = tokenize_korean(sentence)

# 불용어 제거
filtered_tokens = [word for word in tokens if word not in korean_stopwords]

print(filtered_tokens)
