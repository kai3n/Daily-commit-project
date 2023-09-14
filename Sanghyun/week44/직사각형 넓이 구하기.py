def solution(dots): 
    # 너비 구하기
    w = max(dots)[0] - min(dots)[0]
    # 높이 구하기 
    h = max(dots)[1] - min(dots)[1]
    # 직사각형 넓이 반환 
    return w*h