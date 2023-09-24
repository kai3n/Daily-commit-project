def solution(cards):
    # 카드 숫자 저장
    length = len(cards)
    # 방문 했는지 안했는지 체크 용도
    visited = [False]*length
    # 방문할때마다 몇번 탐색하는지 저장
    answer = []
    
    for i in range(length) :
        # 방문한곳을 안했을경우
        if not visited[i] :
            # 인덱스저장 후 카운터 초기화
            idx = i
            cnt = 0
            while not visited[idx] :
                # 방문 후 cnt 갱신 
                cnt += 1
                # 방문 체크
                visited[idx] = True
                # 다음 방문할 인덱스 갱신
                idx = cards[idx] - 1
            # 몇번 방문 했는지 저장
            answer.append(cnt)
    # length 인덱스 마다 몇번씩 방문하는지 정렬 
    answer.sort(reverse = True)
    # 한번에 다 방문이 가능할경우 0을 반화해야하므로 answer에 0을 추가 
    answer.append(0)
    #그룹으로 나누어진 상자들을 곱한 값 반환
    return answer[0]*answer[1]