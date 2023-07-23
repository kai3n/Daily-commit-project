from itertools import combinations
from collections import Counter

def solution(orders, course):
    # 코스 요리 메뉴 저장
    answer = []
    # 몇가지 코스인지 
    for c in course:
        temp = []
        # 한사람당 단품으로 주문한 메뉴
        for order in orders:
            # combinations을 이용해서 코스만큼 조합 
            comb = combinations(sorted(order),c)
            # temp에 저장
            temp +=comb
        # Counter사용해서 빈도수 저장
        counter = Counter(temp)
        # 단품 메뉴가 2이상이여야지 코스에 저장
        if len(counter)!=0 and max(counter.values()) != 1:
            for c in counter:
                # counter에 값이 max값이랑 같으면 제일 많이주문한 메뉴이므로 코스 요리에 저장
                if counter[c] == max(counter.values()):
                    answer.append(''.join(c))
    # 코스요리 이름순으로 정렬해서 반환
    return sorted(answer)