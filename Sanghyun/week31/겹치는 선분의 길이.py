def solution(lines):
    # -100 ~100까지 가능하므로 공간 초기화
    total_space = [0] * 202
    answer =0
    # 값이 있으면 +1 갱신
    for line in lines:
        for i in range(line[0]+1,line[-1]+1): 
            total_space[i+100] += 1
    # 1보다 큰게 있으면 중복이므로 answer 갱신
    for i in range(1,len(total_space)):
        if total_space[i] > 1 :
            answer +=1
    # 중복된 개수 반환
    return answer