from collections import Counter

def solution(array):
    # 빈도수 높은거 두개 저장
    most = Counter(array).most_common(2)
    # most가 1개이면 처음값이 최빈값
    if len(most) == 1:
        return most[0][0]
    # 최빈값이 두개이상이므로 -1 반환
    if most[0][1] == most[1][1]:
        return -1
    # 최빈값 반환
    return most[0][0]