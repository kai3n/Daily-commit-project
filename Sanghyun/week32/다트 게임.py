def solution(dartResult):
    stack = []
    # 10을 A로 변경
    dartResult = dartResult.replace("10", "A")
    # 배수 시킬것 키로 저장
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        # 점수들은 스택에 추가
        if i.isdigit() or i=='A':
            stack.append(10 if i == 'A' else int(i))
        # 보너스로 제곱값 갱ㅅㄴ
        elif i in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** bonus[i])
        # #은 점수 마이너스 
        elif i == '#':
            stack[-1] *= -1
        # 아차상은 해당 점수와 전의 점수를 2배로 갱신
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)
    # 다트 점수 반환
    return sum(stack)