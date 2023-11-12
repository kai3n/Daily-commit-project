def solution(a, b):
    # a가 b 보다크면 갑교체 
    if a > b:
        a, b = b, a
        # a,b까지 합 반환
    return sum(range(a, b + 1))