from collections import defaultdict

def solution(a, b, c, d):
    # 에러방지 디폴트 딕셔너리 선언
    table = defaultdict(int)
    # 값 넣어주기 
    for item in [a,b,c,d]:
        table[item] +=1
    # 값을 기준으로 내림차순으로 정렬 
    table = dict(sorted(table.items(), key = lambda item: item[1], reverse = True))
    # 주사위 값이 다 같으므로 1111곱해서 반환
    if len(table)==1:
        return 1111*a
    # 3개가 같은경우, 2개,2개가 같은경우 나눠서 계산 후 반환
    if len(table) ==2:
        if 2 in table.values():
            return (list(table.keys())[0] + list(table.keys())[1]) * abs(list(table.keys())[0] - list(table.keys())[1])
        else:
            return (10*list(table.keys())[0] + list(table.keys())[1])**2
    # 2개만 같은 경우 나눠서 계산 후 반환
    if len(table)==3:
        return list(table.keys())[1] * list(table.keys())[2]
    # 다 다를때 주사우 최소값 반환
    if len(table)==4:
        return min(table)