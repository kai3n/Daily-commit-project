def solution(s):
    #스택 담을공간 
    stack = []
    for item in s:
        # item이 '('인 경우 스택에 추가 
        if item == '(':
            stack.append(item)
        # item이 ')'인 경우 
        else:
            # stack에 값이 있을때 pop해서 ()짝을 맞춤
            if stack :
                stack.pop()
            # stack에 값이 없을 때는 첫문자로 ')' 이므로 False
            else:
                return False
    # stack에 남아있으면 '(' , ')' 짝이 안맞음
    return len(stack) == 0