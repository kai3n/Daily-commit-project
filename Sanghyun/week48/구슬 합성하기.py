def solution(a,b,c,d,e,f):
    # 결과값 
    answer = True
    # 몇개 합성할수 있는지 저장
    changed_bole =0
    # 현재 있는 구슬중 부족한 구슬 저장
    boles = [a-d,b-e,c-f]

    for bole in boles:
        # 같은색 구슬이 2개 이상 있으면 합성가능하므로 갱신
        if bole>1:
            changed_bole+=bole//2

    for bole in boles:
        # bole 0보다 작으면 부족하므로 합성한것으로 채워줘야함
        if bole<0:
            temp = changed_bole + bole
            changed_bole +=bole
            # 합성한 구슬과 현재 구슬을 합쳐서 0보다 작으면 원하는 구슬을 못얻으므로 false반환
            if temp < 0:
                return False
        else:
            continue
    # 원하는 구슬을 얻을수 있으므로 True반환
    return answer
            