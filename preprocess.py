### 필요한 여러 함수들을 구현하는 파일

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def Cal_tfidf(docs):
    f = open(f'documents/{docs}', 'r', encoding='UTF-8')
    lines = f.read().splitlines()
    f.close()
    print(lines)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(lines)

    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
    return similarities

print(Cal_tfidf("test.txt"))