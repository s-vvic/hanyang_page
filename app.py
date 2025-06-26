def __init__(self):
    self.query = None # 초기에는 쿼리가 없으므로 None으로 설정
    self.query_history = [] # 쿼리 이력을 저장하는 리스트 / 필요 없으면 지워도 됨

def get_user_query(self):
    while True: # 유효한 쿼리를 받을 때까지 반복
        query_input = input("검색할 내용을 입력하세요 (최소 2자 이상): ").strip() # 공백 제거
        if len(query_input) >= 2: # 최소 2자 이상인지 확인
            self.query = self.normalize_query(query_input)

            if self.query in self.query_history:
                  self.query_history.remove(self.query)

            if self.query:
                self.query_history.append(self.query)

            print(f"입력된 검색 쿼리: '{self.query}'")
            print(f"최근 검색 이력 (최신순 정렬): {self.query_history[::-1]}")
            return self.query
        else:
            print("검색 쿼리는 최소 2자 이상이어야 합니다. 다시 입력해주세요.")

def normalize_query(self, query_string):
    return query_string.strip().lower()

# 만약 쿼리를 다른 곳에서 바로 사용하고 싶다면
# print(f"처리할 쿼리: {search_term}")