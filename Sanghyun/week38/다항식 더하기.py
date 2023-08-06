def solution(polynomial):
    # 결과 저장 
    answer = ''
    # 
    sum = 0
    num = 0
    # + 기준으로 먼저 리스트로 바꿈
    polynomial = polynomial.replace(' ', '').split('+')

    for e in polynomial :
        # 만약 x가 있다면 
        if e[-1] == 'x':
            # 1이 아니면 항계수만큼 더해줌
            num += 1 if len(e) == 1 else int(e[:-1:])
        else :
            # x가 없으면 정수를 더해줌
            sum += int(e)
    
    if num>0:
        # x계수가 존재하면 + 까지 answer에 넣어줌
        answer = (str(num) if num>1 else '')+'x'+(' + ' if sum>0 else '')
    # 상수만 계산
    answer += (str(sum) if sum>0 else '')
    # 다항식 계산 반환 
    return answer