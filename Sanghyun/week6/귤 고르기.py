from collections import Counter

def solution(k, tangerine):
    # 최소 몇개의 종류인지 반환
    answer = 0
    # 귤 담는 갯수 
    count = 0
    # 귤 크기 별로 몇개 있는지 Counter생성
    counter = Counter(tangerine)
    # 귤 개수 기준으로 정렬 시켜서 반환
    counter = sorted(counter.values())
    # 귤 담는 갯수가 k보다 작으면 반복
    while count < k:
        # 갯수 많은것부터 담기 시작
        count += counter.pop()
        # 갯수 많은거 담으면 한 종류 담으니깐 +1갱신 
        answer += 1
    # 최소 몇개 종류의 귤을 담는지 반환
    return answer