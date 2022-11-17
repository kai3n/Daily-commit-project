def solution(s):
    # 문자열 리스트로 변환
    s = list(s)
    # 스택 선언
    stack = [] 
    for i in s:
        # 스택이 비어있으면 값 추가 
        if len(stack) == 0 :
            stack.append(i)
        # 스택 마지막값이랑 i랑 비교해서 같으면 스택에서 pop 
        elif stack[-1] == i:
            stack.pop()
        # 앞뒤 문자가 같지 않으므로 stack 추가 
        else :
            stack.append(i)
    # 스택이 비어있으면 짝지어서 문자열 제거 가능 하므로 1반환
    if len(stack)==0:
        return 1
    return 0