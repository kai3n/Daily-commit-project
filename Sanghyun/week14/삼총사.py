from itertools import combinations
# 3명의 학생 번호를 더해서 0이되는 경우의수 개수 출력
def solution(number):
    # 개수 저장
    answer = 0
    # 순열로 number에서 3개로 추출해서 저장 
    comb = list(combinations(number,3))
    # comb반복하면서 합이 0이면 경우의수 갱신
    for item in comb:
        if sum(item) ==0:
            answer+=1
    # 합이 0이 되는 경우의 수 반환
    return answer