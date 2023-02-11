def solution(s):
    # 같은 문자가 얼마나 떨어져 있는지 저장 
    answer = []
    # s크기만큼 반복 
    for i in range(0, len(s)):
        # s문자열에 i인덱스만큼 추출후 길이저장 
        length = len(s[:i])
        # s[:i]에서 s[i] 문자열이 있는지 찾은 후 없으면 -1반환 있으면 인덱스반환 
        index = s[:i].rfind(s[i])
        # 인덱스가 있다면 
        if index != -1:
            # 문자열 길이에서 index뺸값을 저장 
            index = length - index
        # 같은 문자가 얼마나 떨어져 있는지 인덱스마다 저장 
        answer.append(index)
    # 같은 문자가 얼마나 떨어져 있는지 반환
    return answer