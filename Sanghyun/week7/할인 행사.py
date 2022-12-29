from collections import Counter

def solution(want, number, discount):
    # 제품을 할인 받을 수 있는 날짜 일수
    answer = 0
    dic = {}
    # 원하는 제품만큼 반복 
    for i in range(len(want)):
        # 원하는 제품 몇개 필횬자 저장 
        dic[want[i]] = number[i]
    # # 10개 제품 할인받으므로 diccount에서 -9뺴고 반복 
    for i in range(len(discount)-9):
        # 원하는 제품 저장한거랑 10개 할인 딕셔너리로 수로 변환한것과 같으면 제품 할인 한번 받을수 있으므로 answer +1로 갱신 
        if dic == Counter(discount[i:i+10]): 
            answer += 1
    # 제품 할인 받을 수 있는 날짜 반환 
    return answer