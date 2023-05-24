def solution(numbers):
    stack = []
    # -1로 초기화 
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            # stack에 있고 numbers값이 더 크다면 이전 값들 다 갱신 
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            # 스택에 추가 
            stack.append(i)
    # 뒤에 있는 큰 수 리스트 반환
    return answer