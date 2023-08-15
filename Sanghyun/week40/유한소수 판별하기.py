from math import gcd

def solution(a, b):
    # 최대공약수 구해서 b에 나눠주기 
    b //= gcd(a,b)
    # 2,5 로 나눠질때까지 나눔
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    # 만약 b가 1이라면서 유한소수이므로 1 반환 아니면 2반환
    return 1 if b==1 else 2