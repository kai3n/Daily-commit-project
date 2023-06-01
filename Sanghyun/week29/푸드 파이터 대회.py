def solution(food):
    answer = ''
    for i,count in enumerate(food):
        # 제일 처음은 물이므로 다음으로 넘어감 
        if i ==0:
            continue
        # 상대방이랑 같은 갯수로 먹어야하므로 홀수든 짝수든 먹을 갯수 정함
        num = int(count // 2 )
        # 음식을 먹는순서를 차례대로 저장
        for _ in range(num):
            answer+= f'{i}'
    answer_reverse = answer[::-1]
    # 중간에 물이므로 상대방은 오른쪽부터 먹으므로 reverse해서 더한값 반환
    return answer +'0'+answer_reverse