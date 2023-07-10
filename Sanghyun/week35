# 최대 공약수 구하는 함수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(numer1, denom1, numer2, denom2):
    # 분모 계산
    up = numer1 * denom2 + denom1 * numer2
    # 분자 계산
    down = denom1 * denom2
    # 최대공약수 계산
    gcd_value = gcd(up,down)
    # 기약분수로 분수를 더한값 반환
    return [up/gcd_value,down/gcd_value]