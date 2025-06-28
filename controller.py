import model
import numpy as np

QUERY = model.Get_User_Query()
DOCS = model.Search_docs()
PREPROCESS = model.Preprocessing()
BM25 = model.BM_25()

class Controller:
    def execution(self):

        raw_corpus, filenames = DOCS.load_documents_from_folder()

        # 1. 문서 토큰화
        tokenized_corpus = [PREPROCESS.Tokenize(doc) for doc in raw_corpus]

        # 2. 문서 길이 및 평균 길이 계산
        document_lengths = [len(doc) for doc in tokenized_corpus]
        avgdl = sum(document_lengths) / len(document_lengths)

        # 3. IDF 값 계산
        print(tokenized_corpus)
        idf_scores, _ = BM25.compute_idf(tokenized_corpus)

        # 4. 쿼리 준비
        tokenized_query = BM25.tokenize_document(QUERY.get_user_query())

        # 5. 각 문서에 대한 BM25 점수 계산
        scores = []
        for i, doc in enumerate(tokenized_corpus):
            score = BM25.bm25_score(tokenized_query, doc, idf_scores, avgdl)
            scores.append(score)
            print(f"문서 {i} ('{filenames[i]}'): {score:.4f}")

        # 6. 결과 랭킹
        ranked_indices = np.argsort(scores)[::-1]
        print("\n랭킹된 문서 인덱스 (높은 점수부터):", ranked_indices)

        print("\n랭킹된 문서 내용:")
        for idx in ranked_indices:
            print(f"문서 {idx}: {filenames[idx]} (점수: {scores[idx]:.4f})")