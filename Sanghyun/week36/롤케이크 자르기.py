from collections import Counter

def solution(topping):
    # 롤케이크 자르는 방법의 수 저장
    answer = 0
    # topping을 카운터로 저장
    first = Counter(topping)
    # 한개씩 빼서 저장
    second = {}
    
    for i in range(len(topping)) :
        # second에 뺴서 갱신
        if topping[i] in second :
            second[topping[i]] += 1
        else :
            second[topping[i]] = 1
        # second한테 하나 줬으므로 갱신
        first[topping[i]] -= 1
        # first에 토핑이 없으면 값 제거
        if first[topping[i]] == 0 :
            del first[topping[i]]
        # second랑 first의 개수가 같으면 방법의수 갱신
        if len(second) == len(first) :
            answer +=1
    #롤케이크 자르는 방법의수 반환
    return answer