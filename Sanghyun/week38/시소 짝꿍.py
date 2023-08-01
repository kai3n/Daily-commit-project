from collections import Counter

def solution(weights):
    # 몇개 짝궁저장
    answer = 0
    # dictionary로 저장
    counter = Counter(weights)
    
    for k,v in counter.items():
        # 2 이상이면 같은 값이 있으므로 짝궁 추가
        if v>=2:
            answer+= v*(v-1)//2
    # 중복된값 제거
    weights = set(weights) 
    
    for w in weights:
        # 2:3, 2:4, 3:4 비율로 짝궁 만들수 있는지 확인 후 짝궁 개수갱신
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    # 몇개의 짝궁이 나오는지 반환
    return answer