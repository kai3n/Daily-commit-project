def solution(k, score):
    # 명예의 전당에 점수저장
    stack = []
    # 명예의 전당의 최소 점수저장
    answer = []
    for item in score:
        # 명예의 전당에 가수가 없으면 저장후 점수 정렬후 최소점수저장
        if len(stack) !=k:
            stack.append(item)
            stack.sort()
            answer.append(stack[0])
        else:
            # 명예의 전당에 꽉 찼으면 최소 점수인사람 뺀후 높은점수가 명예의 전당에 올라간후 최소점수 저장
            if item > stack[0]:
                stack.pop(0)
                stack.append(item)
                stack.sort()
                answer.append(stack[0])
            else:
                # 점수가 명예의전당보다 낮다면 명예의 전당 최소점수 저장
                answer.append(stack[0])
    # 명예의 전당에 최소점수 반환
    return answer