def solution(cards1, cards2, goal):
    # 인덱스 저장
    i,j = 0,0
    for item in goal:
        # cards[i]이면 item이면 i인덱스 증가
        if len(cards1) > i and cards1[i] == item:
            i +=1
        # cards2에 item이 있으면 j증가
        elif len(cards2) > j and cards2[j] == item:
            j +=1
        # item이 없으면 goal을 못만드므로 No반환
        else:
            return 'No'
    # goal을 만들수 있으므로 Yes반환
    return 'Yes'