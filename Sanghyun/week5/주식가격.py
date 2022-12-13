def solution(prices):
    # 주식 가격이 몇초 동안 안 떨어졌는지 저장
    answer = [0] * len(prices)
    # 초 단위로 기록 된 주식가격 길이 만큼 반복
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            # 1초는 무조건 지나므로 초기 +1로 갱신
            answer[i] +=1
            # 만약 이전주식이 더 비싸다면 떨어진것이므로 break
            if prices[i] > prices[j]:
                break
    # 주식 가격이 몇초동안 안떨어졋는지 반환
    return answer