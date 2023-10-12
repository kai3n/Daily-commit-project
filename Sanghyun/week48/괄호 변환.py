# u,v 나누는 함수
def divide(p):
        # (,) 갯수 비교 
        left, right = 0,0
        for i in range(len(p)):
            # ( 일떄 left값 갱신, 아니면 right값 갱신
            if p[i] == "(":
                left +=1
            else:
                right +=1
            # 같을 때 u,v로 나눠서 반환
            if left == right:
                return p[:i+1] , p[i+1:]
# 올바른 괄호인지 판단
def check(u):
    q = [] 
    for i in u:
        # 초기 q가 없으면 저장
        if not q:
            q.append(i)
        else :
            # i가 ) 이면 q에 맨 마지막값이 (일떄 빼서 제거
            if i ==')' and q[-1]=='(':
                q.pop()
            # 위 조건아닐때 q에 저장
            else:
                q.append(i)
    # q가 있으면 올바른 괄호가 아니므로 false반환
    if q:
        return False
    # q가 없으면 올바른 괄호 이므로 True반환
    return True

def solution(p):
    # p가 빈 문자열이면 p반환
    if p == '':
        return p
    # (,) 개수가 같아질때 u로 나머지 v로 나눔
    u, v = divide(p)
    # u가 올바른 문자이면 재귀
    if check(u):
        return u + solution(v)
    else:
        # 올바른 문자아닐때 재귀 돌린후 ( , ) 값 변경
        answer = '('
        answer += solution(v)
        answer +=')'
        
        u = u[1:-1]
        for i in u:
            if i ==')':
                answer+='('
            else:
                answer +=')'
    # 올바른 괄호로 변환 후 반환
    return answer
