def solution(s):
    # 같은 숫자 제외하고 저장 
    result = []
    for c in s:
        # result에 값이 없거나 이전에 저장한 숫자와 같지 않으면 저장
        if len(result) == 0 or result[-1] != c:
            result.append(c)
    # 반복되는 숫자 제외한 숫자 반환
    return result