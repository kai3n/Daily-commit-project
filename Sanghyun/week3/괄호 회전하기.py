def solution(s):
    # 몇개가 올바른 괄호인지 체크하는 변수
    count= 0 
    # 문자 길이만큼 반복
    for i in range(len(s)):
        # 문자를 왼쪽으로 한칸씩 떙김
        s = s[1:len(s)+1]+s[0]  
        # { , ( , [ 저장하기 위한 stack
        stack=[]
        # 문자가 올바른 괄호 인지 확인하는 변수
        check = True
        # 문자 하나씩 확인 
        for value in s:
            # 만약 열린 괄호 들이 올때는 전부 stack에 추가
            if value =='[' or value =='(' or value =='{':
                stack.append(value)
            else:
                # 스택
                if stack: 
                    # 스택에 있는값 pop으로 꺼내서 저장 
                    temp = stack.pop()
                    # 만약 비교하는 문자열이 )인데 스택에서 pop()값이 ( 아니라면 올바른 괄호가 아님
                    if value ==')' and temp !='(':
                        check = False
                        break
                    # 만약 비교하는 문자열이 ]인데 스택에서 pop()값이 [ 아니라면 올바른 괄호가 아님
                    elif value ==']' and temp !='[':
                        check = False
                        break
                    # 만약 비교하는 문자열이 }인데 스택에서 pop()값이 { 아니라면 올바른 괄호가 아님
                    elif value =='}' and temp !='{':
                        check = False
                        break
                # 스택에 없는 경우는 }}이렇게 오는경우 올바른 괄호가 아님 
                else:
                    check = False
                    break
        # check가 True이고 stack이 비어있으면 올바른 문자이므로 count 갱신
        if check is True and len(stack)<1:
            count+=1
    # 괄호를 왼쪽으로 하나씩 옮겨서 올바른 괄호가 볓개인지 반환
    return count