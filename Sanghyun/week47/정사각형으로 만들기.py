def solution(arr):
    # 행,열 최대값 저장
    max_length = max(len(arr),len(arr[0]))
    # 최대값으로 행,열 값 0으로 갱신
    answer = [[0] *max_length for _ in range(max_length)]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # arr 값 answer에 저장
            answer[i][j] = arr[i][j]
    # arr 정사각형으로 만든후 빈곳은 0으로 채워서 반환
    return answer 
    

    