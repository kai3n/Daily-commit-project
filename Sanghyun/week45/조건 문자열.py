def solution(ineq, eq, n, m):
    # eval로 문자열로 표현된 표현식으로 변환 후 실행
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))