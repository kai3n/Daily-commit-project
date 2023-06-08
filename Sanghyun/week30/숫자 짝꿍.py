def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        # 중복 되는 수를 정렬해서 계속 갱신
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    # 같은게 존재하지 않으므로 -1반환
    if answer == '' :
        return '-1'
    # 00 이 나올경우 0으로 처리 
    elif len(answer) == answer.count('0'):
        return '0'
    else :
    # 문자열에서 중복된 값들 최댓값 반환
        return answer