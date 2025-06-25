import math
from collections import Counter
import numpy as np

def tokenize_document(doc_text):
    """간단한 토큰화 함수 (실제로는 더 복잡한 전처리 필요)"""
    return doc_text.lower().split()

def compute_idf(corpus, k1=1.5, b=0.75):
    """
    코퍼스 내의 각 단어에 대한 IDF (Inverse Document Frequency)를 계산합니다.
    BM25의 IDF는 일반적인 IDF와 약간 다를 수 있지만, 여기서는 일반적으로 사용되는 IDF 정의를 따릅니다.
    """
    num_documents = len(corpus)
    doc_freq = Counter() # 각 단어가 등장하는 문서의 수

    for doc in corpus:
        unique_terms_in_doc = set(doc)
        for term in unique_terms_in_doc:
            doc_freq[term] += 1

    idf_scores = {}
    for term, df in doc_freq.items():
        # 일반적으로 log((N - n + 0.5) / (n + 0.5)) 형태를 사용하기도 합니다.
        idf_scores[term] = math.log((num_documents - df + 0.5) / (df + 0.5) + 1) # +1은 log(1)이 0이 되는 것을 방지

    return idf_scores, doc_freq

def bm25_score(query, document, idf_scores, avgdl, k1=1.5, b=0.75):
    """
    하나의 쿼리와 하나의 문서 간의 BM25 점수를 계산합니다.
    """
    score = 0.0
    doc_len = len(document)
    term_counts = Counter(document) # 문서 내 단어 빈도

    for query_term in query:
        if query_term not in idf_scores:
            continue # 쿼리 단어가 코퍼스에 없으면 스킵

        idf = idf_scores[query_term]
        tf = term_counts[query_term]

        numerator = tf * (k1 + 1)
        denominator = tf + k1 * (1 - b + b * (doc_len / avgdl))

        score += idf * (numerator / denominator)
    return score

# 문서 준비 (텍스트 형태)
raw_corpus = [
    "Hello world, this is a test document.",
    "Hello python programming is fun and exciting.",
    "The world is a great place to live.",
    "This is a test of the BM25 algorithm example.",
]

# 1. 문서 토큰화
tokenized_corpus = [tokenize_document(doc) for doc in raw_corpus]

# 2. 문서 길이 및 평균 길이 계산
document_lengths = [len(doc) for doc in tokenized_corpus]
avgdl = sum(document_lengths) / len(document_lengths)

# 3. IDF 값 계산
idf_scores, _ = compute_idf(tokenized_corpus)

# 4. 쿼리 준비
query_text = "hello test"
tokenized_query = tokenize_document(query_text)

# 5. 각 문서에 대한 BM25 점수 계산
scores = []
for i, doc in enumerate(tokenized_corpus):
    score = bm25_score(tokenized_query, doc, idf_scores, avgdl)
    scores.append(score)
    print(f"문서 {i} ('{' '.join(doc)}'): {score:.4f}")

# 6. 결과 랭킹
ranked_indices = np.argsort(scores)[::-1]
print("\n랭킹된 문서 인덱스 (높은 점수부터):", ranked_indices)

print("\n랭킹된 문서 내용:")
for idx in ranked_indices:
    print(f"문서 {idx}: {raw_corpus[idx]} (점수: {scores[idx]:.4f})")