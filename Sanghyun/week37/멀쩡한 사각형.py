import math

def solution(w,h):
    # w는 가로 h 세로, 1*1 정사각형이있을때 대각선을 그렸을때 선개 안 닿는 정사각형 반환 
    return w*h - (w+h-math.gcd(w,h))