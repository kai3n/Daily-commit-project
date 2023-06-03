def solution(cards1, cards2, goal):
    # cards1, cards2 인덱스로 접근
    i = 0 
    j = 0
    for item in goal:
        # 인덱스가 cards1개수보다 작고 item이랑 맞으면 인덱스 올려줌
        if len(cards1) > i and cards1[i] == item:
            i +=1
        # 인덱스가 cards2개수보다 작고 item이랑 맞으면 인덱스 올려줌
        elif len(cards2) > j and cards2[j] == item:
            j +=1
        # 위경우 아니면 No 반환
        else:
            return 'No'
    # 순서대로 goal을 만들수 있으므로 Yes반환
    return 'Yes'