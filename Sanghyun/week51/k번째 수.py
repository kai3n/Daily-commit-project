def solution(array, commands):
    answer = []
    for command in commands:
        # 시작, 끝 인덱스, k번쨰 수 저장
        i,j,k = command
        # 시작, 끝 인덱스 사이값들을 정렬후 k번쨰 수 answer에 저장
        answer.append(list(sorted(array[i-1:j]))[k-1])
    # k번째 수 반환
    return answer