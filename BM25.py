from rank_bm25 import BM25Okapi
import numpy as np

# 1. 문서 준비 (이미 토큰화된 형태여야 함)
# 실제 시나리오에서는 NLTK, KoNLPy (한국어), SpaCy 등으로 토큰화합니다.
corpus = [
    ["hello", "world", "this", "is", "a", "test"],
    ["hello", "python", "programming", "is", "fun"],
    ["world", "is", "a", "great", "place"],
    ["test", "bm25", "algorithm", "example"],
]

# 2. BM25 모델 초기화
# k1과 b는 BM25 알고리즘의 파라미터입니다.
# 기본값은 k1=1.5, b=0.75 입니다.
bm25 = BM25Okapi(corpus)

# 3. 쿼리 준비 (토큰화된 형태)
query = ["hello", "test"]

# 4. 쿼리와 각 문서 간의 점수 계산
# BM25Okapi.get_scores() 메서드는 각 문서에 대한 BM25 점수 배열을 반환합니다.
doc_scores = bm25.get_scores(query)

print("문서별 BM25 점수:", doc_scores)

# 5. 점수를 기준으로 문서 랭킹 (선택 사항)
# 점수가 높은 문서부터 정렬하여 관련성 높은 문서를 찾습니다.
ranked_docs_indices = np.argsort(doc_scores)[::-1]
print("\n랭킹된 문서 인덱스 (높은 점수부터):", ranked_docs_indices)

print("\n랭킹된 문서 내용:")
for idx in ranked_docs_indices:
    print(f"문서 {idx}: {' '.join(corpus[idx])} (점수: {doc_scores[idx]:.4f})")

# 다른 쿼리로 테스트
query2 = ["python", "algorithm"]
doc_scores2 = bm25.get_scores(query2)
print(f"\n쿼리 '{' '.join(query2)}'에 대한 문서별 BM25 점수:", doc_scores2)
ranked_docs_indices2 = np.argsort(doc_scores2)[::-1]
print("랭킹된 문서 인덱스:", ranked_docs_indices2)