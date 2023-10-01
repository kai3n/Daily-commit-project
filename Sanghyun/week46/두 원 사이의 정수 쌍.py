from math import sqrt

def solution(r1, r2):
    # 1사분면 정수만 저장
    quar = 0
    for i in range(0, r1):
        # r2가 반지름이 원에서 r1반지름의 원만큼 빼서 교점이 있을경우 -1해서 저장
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        # r2 ,r1 사이에 있는 값들 저장 
        quar += int(sqrt(r2**2 - i**2))
    # 1사분면에서 전체적으로 *4해서 원 사이의 정수 반환
    return quar * 4