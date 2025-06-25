### 필요한 여러 함수들을 구현하는 파일

### 문서의 tf-idf 벡터화에 필요한 module
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

### 문서 데이터의 전처리에 필요한 module
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

def Cal_tfidf(docs):
    f = open(f'documents/{docs}', 'r', encoding='UTF-8')
    lines = f.read().replace("\n"," ").replace(".","\n").splitlines()
    f.close()

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(lines)

    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix)
    return similarities

def Data_Preprocessing():
    # NLTK Data 다운로드
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # 텍스트 데이터
    text = "This is an example sentence. It contains some words and punctuation!"

    # 1. 정제 (소문자 변환 및 특수 문자 제거)
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # 2. 토큰화
    tokens = word_tokenize(text)

    # 3. 불용어 제거
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # 4. 어간 추출 (Porter Stemmer 사용)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    # 5. 표제어 추출 (WordNetLemmatizer 사용)
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    print("원문:", text)
    print("토큰화:", tokens)
    print("불용어 제거:", filtered_tokens)
    print("어간 추출:", stemmed_tokens)
    print("표제어 추출:", lemmatized_tokens)

### test code
#print(Cal_tfidf("test.txt"))
Data_Preprocessing()